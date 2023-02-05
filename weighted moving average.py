def wma(tradeInfo):
    # Split Trade Info String
    trades = tradeInfo.split(';')

    # Dictionary To Hold WMA Data
    wmaData = {}

    # Current Sequence Number
    curSeqNum = -1

    # For Each Trade
    for trade in trades:
        # Split Trade String Into Individual Data
        data = trade.split(',')
        key = int(data[0])
        value = float(data[1])
        quantity = float(data[2])
        seqNum = int(data[3])

        # Check If Sequence Number Is Greater Than Previous One
        if seqNum > curSeqNum:
            curSeqNum = seqNum
        else:
            # If No Skip Rest Of The Loop
            continue

        # If There Is Already M(x) Data In  Dictionary
        if key in wmaData:
            # Get M(x) & Q(x)
            (oldVal, oldQuantity) = wmaData[key]
            # Calculate Q(x+1)
            totalQuantity = oldQuantity + quantity
            # Calculate And Replace Old M(x) & Q(x)
            wmaData[key] = ((((oldVal * oldQuantity) + (value * quantity)) / totalQuantity), totalQuantity)
        else:
            # If There Is No M(x) Data In  Dictionary
            # Calculate And Create Entry For M(x) & Q(x)
            wmaData[key] = (((value * quantity) / quantity), quantity)
        # Print Result
        printKeyAndWMA(key, wmaData[key][0])


# Print WMA
def printKeyAndWMA(key, weightedMovingAverage):
    print(str(key) + ": {:0.2f}".format(weightedMovingAverage))


# Test Code
testCases = [
    "1,2000,5,1;1,2030,15,2;1,2000,10,1;2,2050,15,5;1,2067,8,6;2,2050,5,7",
    "1,2000,5,1;1,2050,5,2;2,3000,10,3",
    "1,2000,5,2;1,2050,5,4",
    "1,2000,5,3;2,2040,5,2"
]

for test in testCases:
    print(f"Input: {test}\nOutput:")
    wma(test)
    print()
