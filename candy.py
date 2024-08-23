ratings = [1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]

def findPeakLeft(i, ratings, candies):
        
    candies[i] = candies[i + 1] + 1

    if i == 0 or ratings[i - 1] <= ratings[i] or candies[i - 1] > candies[i]:
        return candies
    return findPeakLeft(i - 1, ratings, candies)
    
    
def findPeakRight(i, ratings, candies):

    candies[i] = candies[i - 1] + 1

    if i == len(ratings) - 1 or ratings[i + 1] <= ratings[i] or candies[i + 1] > candies[i]:
        return candies
    return findPeakRight(i + 1, ratings, candies)

    
def findPeaks(i, ratings, candies):

    if len(ratings) == 1:
        return candies
    
    if i == len(ratings) - 1:
        if ratings[i - 1] > ratings[i]:
            return findPeakLeft(i - 1, ratings, candies)
        else:
            return candies

    if i == 0:
        if ratings[i + 1] > ratings[i]:
            return findPeakRight(i + 1, ratings, candies)
        else:
            return candies
    
    if ratings[i - 1] > ratings[i] <= ratings[i + 1] and candies[i - 1] <= candies[i]:
        candies = findPeakLeft(i - 1, ratings, candies)
    if ratings[i + 1] > ratings[i] <= ratings[i - 1] and candies[i + 1] <= candies[i]:
        candies = findPeakRight(i + 1, ratings, candies)
    
    return candies



def giveCandy(ratings):

    # Find the troughs in the arrays
    # Assign each trough to be worth one candy
    # On either side of the trough, give out one more candy to each higher neighbour, until a peak is reached.
    # A trough is any child that has no neighbour with a lower rating
    # A peak is any child that has no neighbour with a higher rating

    candies = [1] * len(ratings)

    for i in range(len(ratings)):
        print(i)
        candies = findPeaks(i, ratings, candies)
        print(candies)

    return sum(candies)

giveCandy(ratings)

#j = 12001
#for i in reversed(range(len(ratings))):
#    if i < j:
#        print(i)
#        j = i
#    else:
#        break