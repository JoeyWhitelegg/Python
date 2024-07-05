# write the Windows security event log to a plaintext file

import win32evtlog
import win32evtlogutil
import win32security
import os
import traceback

# get_event_logs read event logs from specified servers and log types to extract relevant info
def get_event_logs(server, log_type):
    logs = []
    try:
        hand = win32evtlog.OpenEventLog(server, log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total = win32evtlog.GetNumberOfEventLogRecords(hand)

        while True:
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            if not events:
                break
            for event in events:
                log = {'EventID': event.EventID,
                    'EventType': event.EventType,
                    'TimeGenerated': event.TimeGenerated.Format(),
                    'SourceName': event.SourceName,
                    'EventCategory': event.EventCategory,
                    'ComputerName': event.ComputerName,
                    'User': None}
            
                if event.Sid is not None:
                    try:
                        user, domain, _ = win32security.LookupAccountSid(None, event.Sid)
                        log['User'] = f"{domain}\\{user}"
                    except Exception as e:
                        log['User'] = f"Unknown User (SID: {event.Sid})"
                
                logs.append(log)
        win32evtlog.CloseEventLog(hand)
    except Exception as e:
        print(f"Failed to read event logs: (e)")
        traceback.print_exc()
    return logs

# write_logs_to_file writes extracted logs to a plaintext file
def write_logs_to_file(logs, file_path):
    with open(file_path, 'w') as f:
        for log in logs:
            f.write(f"EventID:{log['EventID']}\n")
            f.write(f"EventType: {log['EventType']}\n")
            f.write(f"TimeGenerated: {log['TimeGenerated']}\n")
            f.write(f"SourceName: {log['SourceName']}\n")
            f.write(f"EventCategory: {log['EventCategory']}\n")
            f.write(f"ComputerName: {log['ComputerName']}\n")
            f.write(f"User: {log['User']}\n")
            f.write(f"{'-'*40}\n")

if __name__ == "__main__":
    server = None # None means local machine
    log_type = "Security"
    output_file = "security_log.txt"

    # the security logs are written to the file security_log.txt
    logs = get_event_logs(server, log_type)
    if logs:
        write_logs_to_file(logs, output_file)
        print(f"Security log has been written to {output_file}")
    else:
        print("No logs found or failed to read logs.")
        
