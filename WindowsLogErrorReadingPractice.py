import win32evtlog
import datetime

# open Windows Security event log
winSecLog = win32evtlog.OpenEventLog(None, "Security")

# read events from the log
flags = win32evtlog.EVENTLOG_SEQUENTIAL_READ
events = win32evtlog.ReadEventLog(winSecLog, flags, 0)

# define list for events
Thursday_events = []
nonThursday_events = []

# iterate through events
while True:
    event = win32evtlog.GetNextEvent(winSecLog, flags)
    if not event:
        break

# check if event is successful login, 4624 = successful login, and get date
    if event.EventID == 4624:
        # get timestamp
        timestamp = event.TimeGenerated.Format()
    # check if event is a failed login attempt, 4625 = failed logins
    if event.EventID == 4625:
        # get timestamp
        timestamp = event.TimeGenerated.Format()

        # convert timestamp to datetime object
        timestamp_datetime = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        # occured on Thursday, add data to list
        if timestamp_datetime.weekday() == 3:   # thursday = 3, wednesday = 2, tuesday = 1, etc.
            # flag failed login
            if event.ID == 4625:
                usernameFail = event.StringInserts[5]
                # record the data stored in "StringInserts" (important are IP address and login attempts) in the Thursday_events list
                Thursday_events.append(f'{timestamp}:{usernameFail}')

           ''' # flag success login for future reference
            if event.ID == 4624:
                usernameSuccess = event.StringInserts[5]
                # record the data stored in "StringInserts" in the Thursday_events
                Thursday_events.append(f'{timestamp}:{usernameSuccess}')'''

                # save info to report
                reportDoc = open("Weekly_Update.txt", "w")
                for event in Thursday_events:
                    reportDoc.append("Thursday logins on Windows: ", timestamp + usernameFail + "\n")
                    # no need to append the success attempts as of yet
         
         # not occured on Thursday, add data to list
        if timestamp_datetime.weekday() != 3:   # thursday = 3, wednesday = 2, tuesday = 1, etc.
            # flag failed login
            if event.ID != 4625:
                break
            if event.ID == 4625:
                username = event.StringInserts[5]
                # record the data stored in "StringInserts" in the nonThursday_events
                nonThursday_events.append(f'{timestamp}:{username}')

                # save info to report
                reportDoc = open("Weekly_Update.txt", "w")
                for event in nonThursday_events:
                    reportDoc.append("Non-Thursday login attempts on Windows: ", timestamp + username + "\n")

# close event log
win32evtlog.CloseEventLog(winSecLog)