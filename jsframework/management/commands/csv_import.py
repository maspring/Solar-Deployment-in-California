from django.core.management.base import BaseCommand
from jsframework.models import Deployment, Statistics
from datetime import datetime
import csv, os

statistics = []

def findYear (inputRow):
    if inputRow[22] != '':
        thisDate = datetime.strptime(inputRow[22], "%Y-%m-%d").date() # format is "%m/%d/%Y" after Excel saves it
        print ("the year is (1): ", thisDate.year)
    elif inputRow[24] != '':
        thisDate = datetime.strptime(inputRow[24], "%Y-%m-%d").date()
        print ("the year is (2): ", thisDate.year)
    elif inputRow[33] != '':
        thisDate = datetime.strptime(inputRow[33], "%Y-%m-%d").date() # format is "%Y-%m-%d" if Excel has not saved it
        print ("the year is (3): ", thisDate.year)
    elif inputRow[39] != '':
        thisDate = datetime.strptime(inputRow[39], "%Y-%m-%d").date()
        print ("the year is (4): ", thisDate.year)
    else:
        print ("-----------------------------------------------------")

    return thisDate

def findPosition(dateObject):
    if dateObject.year == 2006:
        position = 7
    elif dateObject.year == 2007:
        position = 11
    elif dateObject.year == 2008:
        position = 15
    elif dateObject.year == 2009:
        position = 19
    elif dateObject.year == 2010:
        position = 23
    elif dateObject.year == 2011:
        position = 27
    elif dateObject.year == 2012:
        position = 31
    elif dateObject.year == 2013:
        position = 35
    elif dateObject.year == 2014:
        position = 39
    elif dateObject.year == 2015:
        position = 43
    else:
        position = 10000

    print ("year= ", dateObject.year, " position = ", position)

    return position


class Command(BaseCommand):
    def handle(self, *args, **options):
        statistics = []
        statisticsRow = []
        matchFound = False

        with open('test.csv', 'rb') as csvfile:
            fields = csv.reader(csvfile, dialect='excel', delimiter=',', quotechar='"')


            # Exercise Names
            for row, deployment in enumerate(fields):
                identifier = deployment
                # print dir(identifier)
                # print identifier
                # print identifier[0]
                # print identifier[1]
                # print identifier[6]
                # print identifier[7]
                # print identifier[8]
                # print identifier[17] # sector
                # print identifier[18]
                # print identifier[19]
                # print identifier[20] # state
                # print identifier[21] # zip code
                # print identifier[22] # first request date
                # print identifier[24] # first review date
                # print identifier[33] # confirmed reservation date
                # print identifier[39] # first completed date
                # print identifier[46] # seller
                # print identifier[109] # azimuth
                # print identifier[110] # tilt
                # print identifier[111] # tracking


                if row > 0 and identifier[17] == "Residential":


                    # This conversion is only necessary when Excel has saved the file. Must change formats to what postgres expects

                    # if identifier[22] != '':
                    #     identifier[22] = datetime.strptime(identifier[22], "%m/%d/%Y").date # .strftime("%Y-%m-%d")
                    # identifier[22] = "2010-01-01"
                    # print ("reformatted date looks like this: ", identifier[22])
                    # else:
                    #     identifier[22] = 1970-01-01
                    #     print ("else : ", identifier[22])

                    if identifier[8] == '':
                        identifier[8] = 1.0


                    # Deployment elements we will save
                    # Deployment.objects.create(
                    #     application = identifier[0],
                    #     utility = identifier[1],
                    #     incentive = identifier[6],
                    #     cost = identifier[7],
                    #     rating = identifier[8], # convert string to float
                    #     sector = identifier[17],
                    #     city =	identifier[18],
                    #     county = identifier[19],
                    #     state = identifier[20],
                    #     zipcode = identifier[21],
                    #     # firstdate = unicode(identifier[22]),
                    #     # seconddate = unicode(identifier[24]),
                    #     # thirddate = unicode(identifier[33]),
                    #     # fourthdate = unicode(identifier[39]),
                    #     seller = identifier[46],
                    #     azimuth = identifier[109],
                    #     tilt = identifier[110],
                    #     tracking = identifier[111],
                    # )


                    for rowNumber, deploymentRow in enumerate(statistics):
                        thisZip = identifier[21]
                        if identifier[7] != '':
                            thisCost = float(identifier[7])
                        else:
                            thisCost = 0.0
                        if identifier[8] != '':
                            thisRating = float(identifier[8])
                        else:
                            thisRating = 100.0
                        if thisZip == deploymentRow[0]:
                            deploymentRow[1] = deploymentRow[1] + thisRating
                            deploymentRow[3] = deploymentRow[3] + 1
                            thisDateObject = findYear(identifier)
                            thisPosition = findPosition(thisDateObject)
                            deploymentRow[thisPosition] = deploymentRow[thisPosition] + 1
                            deploymentRow[thisPosition -3] = deploymentRow[thisPosition -3] + thisCost
                            deploymentRow[thisPosition -2] = deploymentRow[thisPosition -2] + thisRating
                            deploymentRow[thisPosition -1] = round(((deploymentRow[thisPosition -3] / deploymentRow[thisPosition -2]) / 1000),2)
                            matchFound = True
                            print("match found")

                    if matchFound != True:
                        thisZip = identifier[21]
                        if identifier[7] != '':
                            thisCost = float(identifier[7])
                        else:
                            thisCost = 0.0
                        if identifier[8] != '':
                            thisRating = float(identifier[8])
                        else:
                            thisRating = 100.0
                        cityName = identifier[18]
                        statisticsRow = [thisZip, thisRating, cityName, 1,
                                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        thisDateObject = findYear(identifier)
                        thisPosition = findPosition(thisDateObject)
                        statisticsRow[thisPosition] = 1
                        statisticsRow[thisPosition-3] = thisCost
                        statisticsRow[thisPosition-2] = thisRating
                        statisticsRow[thisPosition-1] = round(((thisCost / thisRating) / 1000),2)
                        statistics.append(statisticsRow)
                        print("newline added")
                    else:
                        matchFound = False

            # print statistics
                    print ("the row is: ", row)


            # print  statisticsRow


                    #     application = identifier[0],


        # for index, thisZipcode in enumerate(statistics):
        #
        #     print("thisZipcode = ", thisZipcode)
        #     # Statistics elements we will save
        #     Statistics.objects.create(
        #         zipcode = thisZipcode[0],
        #         totalProduction = thisZipcode[1],
        #         city = thisZipcode[2],
        #         totalDeployments = thisZipcode[3],
        #         costOhSix = thisZipcode[4],
        #         productionOhSix = thisZipcode[5],
        #         costPerWattOhSix = thisZipcode[6],
        #         deploymentsOhSix = thisZipcode[7],
        #         costOhSeven = thisZipcode[8],
        #         productionOhSeven = thisZipcode[9],
        #         costPerWattOhSeven = thisZipcode[10],
        #         deploymentsOhSeven = thisZipcode[11],
        #         costOhEight = thisZipcode[12],
        #         productionOhEight = thisZipcode[13],
        #         costPerWattOhEight = thisZipcode[14],
        #         deploymentsOhEight = thisZipcode[15],
        #         costOhNine = thisZipcode[16],
        #         productionOhNine = thisZipcode[17],
        #         costPerWattOhNine = thisZipcode[18],
        #         deploymentsOhNine = thisZipcode[19],
        #         costTen = thisZipcode[20],
        #         productionTen = thisZipcode[21],
        #         costPerWattTen = thisZipcode[22],
        #         deploymentsTen = thisZipcode[23],
        #         costEleven = thisZipcode[24],
        #         productionEleven = thisZipcode[25],
        #         costPerWattEleven = thisZipcode[26],
        #         deploymentsEleven = thisZipcode[27],
        #         costTwelve = thisZipcode[28],
        #         productionTwelve = thisZipcode[29],
        #         costPerWattTwelve = thisZipcode[30],
        #         deploymentsTwelve = thisZipcode[31],
        #         costThirteen = thisZipcode[32],
        #         productionThirteen = thisZipcode[33],
        #         costPerWattThirteen = thisZipcode[34],
        #         deploymentsThirteen = thisZipcode[35],
        #         costFourteen = thisZipcode[36],
        #         productionFourteen = thisZipcode[37],
        #         costPerWattFourteen = thisZipcode[38],
        #         deploymentsFourteen = thisZipcode[39],
        #         costFifteen = thisZipcode[40],
        #         productionFifteen = thisZipcode[41],
        #         costPerWattFifteen = thisZipcode[42],
        #         deploymentsFifteen = thisZipcode[43]
        #     )


        columnHeadings = ["zipcode", "totalProduction", "city", "totalDeployments",
                          "costOhSix", "productionOhSix", "costPerWattOhSix", "deploymentsOhSix",
                          "costOhSeven", "productionOhSeven", "costPerWattOhSeven", "deploymentsOhSeven",
                          "costOhEight", "productionOhEight", "costPerWattOhEight", "deploymentsOhEight",
                          "costOhNine", "productionOhNine", "costPerWattOhNine", "deploymentsOhNine",
                          "costTen", "productionTen", "costPerWattTen", "deploymentsTen",
                          "costEleven", "productionEleven", "costPerWattEleven", "deploymentsEleven",
                          "costTwelve", "productionTwelve", "costPerWattTwelve", "deploymentsTwelve",
                          "costThirteen", "productionThirteen", "costPerWattThirteen", "deploymentsThirteen",
                          "costFourteen", "productionFourteen", "costPerWattFourteen", "deploymentsFourteen",
                          "costFifteen", "productionFifteen", "costPerWattFifteen", "deploymentsFifteen",
                          ]

        statistics.insert(0, columnHeadings)

        with open('eggs.csv', 'wb') as csvfile:
            newFile = csv.writer(csvfile, delimiter=',', quotechar='"')

            newFile.writerows(statistics)