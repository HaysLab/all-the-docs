import torch
from torch import nn, optim
from torch.autograd import Variable
import torchvision
from torchvision import transforms
from torchvision.models import resnet18
from tqdm import tqdm


use_cuda = True

def get_dataset():
    print("Preparing dataset...")
    train_transforms = transforms.Compose([
        transforms.RandomCrop(32, padding=4),  # CIFAR images are 32x32
        transforms.RandomHorizontalFlip(),
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])
    test_transforms = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),        
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])

    train = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transforms)
    trainloader = torch.utils.data.DataLoader(train, batch_size=128, shuffle=True, num_workers=2)

    test = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=test_transforms)
    testloader = torch.utils.data.DataLoader(test, batch_size=100, shuffle=False, num_workers=2)

    print("Dataset ready!")
    return trainloader, testloader


def get_model():
    print("Building model")
    model = resnet18(pretrained=True)
    if use_cuda:
        model.cuda()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.9, weight_decay=5e-4)
    
    print("Model is ready.")
    return model, criterion, optimizer


def train(model, criterion, optimizer, dataloader, start=0, epochs=5):
    model.train()

    for i in range(start, epochs):
        train_loss = 0

        for idx, (inputs, targets) in tqdm(enumerate(dataloader), total=len(dataloader)):
            inputs, targets = Variable(inputs), Variable(targets)
            if use_cuda:
                inputs, targets = inputs.cuda(), targets.cuda()
            
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            # Zero out the gradients since they accumulate over batches
            optimizer.zero_grad()
            loss.backward()

            # Record the loss
            train_loss += loss.data[0]

            # Take an optimization step
            optimizer.step()

        print("Training loss: ", train_loss/len(dataloader))

    print("Finished training")


def test(model, dataloader):
    model.eval()

    test_loss = 0
    total = 0
    correct = 0

    for idx, (inputs, targets) in tqdm(enumerate(dataloader), total=len(dataloader)):
        inputs, targets = Variable(inputs), Variable(targets)
        if use_cuda:
            inputs, targets = inputs.cuda(), targets.cuda()
        
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # Record the loss
        test_loss += loss.data[0]

        _, predicted = torch.max(outputs.data, 1)
        total += targets.size(0)
        correct += predicted.eq(targets.data).cpu().sum()

    print("Test loss: ", test_loss/len(dataloader))
    print("Accuracy: ", 100.0 * correct/total)


if __name__ == "__main__":
    trainloader, testloader = get_dataset()
    model, criterion, optimizer = get_model()

    train(model, criterion, optimizer, trainloader)
    test(model, testloader)
