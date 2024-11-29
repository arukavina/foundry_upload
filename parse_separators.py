header_rows = 'AttendanceDate ShiftDate  HigherSiteCode  HigherSiteName                 SiteCode    SiteBrand            Source          DepartmentName                                     EmployeeId                                         RecordTypeDesc                                                                                       PayRate               StartTime               EndTime                 Hour   AttendanceValue                         WorkedTimeHrs'
input_string = "-------------- ---------- --------------- ------------------------------ ----------- -------------------- --------------- -------------------------------------------------- -------------------------------------------------- ---------------------------------------------------------------------------------------------------- --------------------- ----------------------- ----------------------- ------ --------------------------------------- ---------------------------------------"
data_string = "AAAAA           ---------- ------           ------------------------------ ----------- -------------------- --------------- -------------------------------------------------- -------------------------------------------------- ---------------------------------------------------------------------------------------------------- --------------------- ----------------------- ----------------------- ------ --------------------------------------- ---------------------------------------"

# Split the string into parts by spaces
parts = input_string.split(" ")

# Calculate initial positions using cumulative lengths
positions = list(map(len, parts))
start_positions = [sum(positions[:i]) + i for i in range(len(parts))]

# Filter out non-dash segments and calculate start and end positions
segments = list(
    map(
        lambda i: [start_positions[i], start_positions[i] + len(parts[i])],
        filter(lambda i: '-' in parts[i], range(len(parts))),
    )
)

# headers = ['SourceFile', 'BusinessDate', 'HigherSiteCode', 'HigherSiteName','SiteBrand', 'posItemCode', 'oductShortName','Qty', 'SalesValueBase']
headers = [header_rows[segment[0]:segment[1]].strip() for segment in segments]
print(headers)
values = [data_string[segment[0]:segment[1]].strip() for segment in segments]
print(dict(zip(headers, values)))