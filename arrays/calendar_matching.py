
'''
Imagine that you want to schedule a meeting of a certain duration with a co-worker. You have access to your calendar and your co-worker's
calendar (both of which contain your respective meetings for the day, in the form of [startTime, endTime] ), as well as both of your daily
bounds (i.e., the earliest and latest times at which you're available for meetings every day, in the form of [earliestTime, latestTime] ).
Write a function that takes in your calendar, your daily bounds, your co-worker's calendar, your co-worker's daily bounds, and the duration of
the meeting that you want to schedule, and that returns a list of all the time blocks (in the form of [startTime, endTime] ) during which
you could schedule the meeting, ordered from earliest time block to latest.
Note that times will be given and should be returned in military time. For example: 8:30 , 9:01 , and 23:56 .
Also note that the given calendar times will be sorted by start time in ascending order, as you would expect them to appear in a calendar
application like Google Calendar.
Sample Input
calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30
Sample Output
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
'''



def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatecal1 = updateCalendar(calendar1,dailyBounds1)
    updatecal2 = updateCalendar(calendar2,dailyBounds2)
    mergedCal = mergeCalendar(updatecal1, updatecal2)
    flatenedCal = flatCalendar(mergedCal)
    return getMatchingAvailability(flatenedCal, meetingDuration)

def updateCalendar(calendar, daily):
    updatedCalendar = calendar[:]
    updatedCalendar.insert(0, ['0:00', daily[0]])
    updatedCalendar.append([daily[1], '23:59'])
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])],updatedCalendar))

def mergeCalendar(calendar1, calendar2):
    merged = []
    i, j = 0,0
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]

        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i +=1
        else:
            merged.append(meeting2)
            j +=1
    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1
    return merged

def flatCalendar(calendar):
    flatened = [calendar[0][:]]
    for i in range(1, len(calendar)):
        currentMeeting = calendar[i]
        prevMeeting = flatened[-1]
        curStart, curEnd = currentMeeting
        prevStart, prevEnd = prevMeeting

        if prevEnd > curStart:
            newPrev = [prevStart, max(prevEnd, curEnd)]
            flatened[-1] = newPrev
        else:
            flatened.append(currentMeeting[:])
    return flatened

def getMatchingAvailability(calendar, duration):
    matchinavailabilities = []
    for i in range(1, len(calendar)):
        start = calendar[i-1][1]
        end = calendar[i][0]
        avaliabilityDuration = end - start
        if avaliabilityDuration >= duration:
            matchinavailabilities.append([start, end])
    return list(map(lambda m: [minitesToHours(m[0]), minitesToHours(m[1])],matchinavailabilities))


def minitesToHours(time):
    hours = time // 60
    minutes = time % 60

    hoursString = str(hours)
    minutesString = "0" + str(minutes) if minutes < 10 else str(minutes)

    return hoursString + ":" + minutesString

    
def timeToMinutes(time):
    hours, minutes = list(map(int,time.split(":")))
    return hours * 60 + minutes
    


calendar1 = [
            ["7:00", "7:45"],
            ["8:15", "8:30"],
            ["9:00", "10:30"],
            ["12:00", "14:00"],
            ["14:00", "15:00"],
            ["15:15", "15:30"],
            ["16:30", "18:30"],
            ["20:00", "21:00"],
        ]
dailyBounds1 = ["6:30", "22:00"]
calendar2 = [["9:00", "10:00"], ["11:15", "11:30"], ["11:45", "17:00"], ["17:30", "19:00"], ["20:00", "22:15"]]
dailyBounds2 = ["8:00", "22:30"]
meetingDuration = 30

print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))



import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:00", "20:00"]
        calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
        dailyBounds2 = ["10:00", "18:30"]
        meetingDuration = 30
        expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_2(self):
        calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:00", "20:00"]
        calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
        dailyBounds2 = ["10:00", "18:30"]
        meetingDuration = 45
        expected = [["15:00", "16:00"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_3(self):
        calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["8:00", "20:00"]
        calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
        dailyBounds2 = ["7:00", "18:30"]
        meetingDuration = 45
        expected = [["8:00", "9:00"], ["15:00", "16:00"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_4(self):
        calendar1 = [["8:00", "10:30"], ["11:30", "13:00"], ["14:00", "16:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["8:00", "18:00"]
        calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
        dailyBounds2 = ["7:00", "18:30"]
        meetingDuration = 15
        expected = []
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_5(self):
        calendar1 = [["10:00", "10:30"], ["10:45", "11:15"], ["11:30", "13:00"], ["14:15", "16:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:30", "20:00"]
        calendar2 = [["10:00", "11:00"], ["12:30", "13:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
        dailyBounds2 = ["9:00", "18:30"]
        meetingDuration = 15
        expected = [["9:30", "10:00"], ["11:15", "11:30"], ["13:30", "14:15"], ["18:00", "18:30"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_6(self):
        calendar1 = [["10:00", "10:30"], ["10:45", "11:15"], ["11:30", "13:00"], ["14:15", "16:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:30", "20:00"]
        calendar2 = [["10:00", "11:00"], ["10:30", "20:30"]]
        dailyBounds2 = ["9:00", "22:30"]
        meetingDuration = 60
        expected = []
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_7(self):
        calendar1 = [["10:00", "10:30"], ["10:45", "11:15"], ["11:30", "13:00"], ["14:15", "16:00"], ["16:00", "18:00"]]
        dailyBounds1 = ["9:30", "20:00"]
        calendar2 = [["10:00", "11:00"], ["10:30", "16:30"]]
        dailyBounds2 = ["9:00", "22:30"]
        meetingDuration = 60
        expected = [["18:00", "20:00"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_8(self):
        calendar1 = []
        dailyBounds1 = ["9:30", "20:00"]
        calendar2 = []
        dailyBounds2 = ["9:00", "16:30"]
        meetingDuration = 60
        expected = [["9:30", "16:30"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_9(self):
        calendar1 = []
        dailyBounds1 = ["9:00", "16:30"]
        calendar2 = []
        dailyBounds2 = ["9:30", "20:00"]
        meetingDuration = 60
        expected = [["9:30", "16:30"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_10(self):
        calendar1 = []
        dailyBounds1 = ["9:30", "16:30"]
        calendar2 = []
        dailyBounds2 = ["9:30", "16:30"]
        meetingDuration = 60
        expected = [["9:30", "16:30"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

    def test_case_11(self):
        calendar1 = [
            ["7:00", "7:45"],
            ["8:15", "8:30"],
            ["9:00", "10:30"],
            ["12:00", "14:00"],
            ["14:00", "15:00"],
            ["15:15", "15:30"],
            ["16:30", "18:30"],
            ["20:00", "21:00"],
        ]
        dailyBounds1 = ["6:30", "22:00"]
        calendar2 = [["9:00", "10:00"], ["11:15", "11:30"], ["11:45", "17:00"], ["17:30", "19:00"], ["20:00", "22:15"]]
        dailyBounds2 = ["8:00", "22:30"]
        meetingDuration = 30
        expected = [["8:30", "9:00"], ["10:30", "11:15"], ["19:00", "20:00"]]
        result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()