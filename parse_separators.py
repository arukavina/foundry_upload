header_rows = 'BusinessDate WeekNumber  TransactionTime  HourofDay   Highersitecode  HigherSitename                 Source          SiteBrand            CashierCode     transactionNo        LineNum     ProductShortName                                                                                     PLU             posDepartmentCode posDepartmentName                                  OrderChannel                                                                                         OrderChannel2                                                                                        OrderDevice                                                                                          OrderMethod                                                                                          OrderMethodDescription                                                                               SaleTypeCode Qty                                     Total'
input_string = "------------ ----------- ---------------- ----------- --------------- ------------------------------ --------------- -------------------- --------------- -------------------- ----------- ---------------------------------------------------------------------------------------------------- --------------- ----------------- -------------------------------------------------- ---------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ------------ --------------------------------------- ---------------------"
data_string = "2024-01-01   1           13:53:00.0000000 13          39004           Commodore Perry                pdi-iris        Applegreen           39004-0012972   1013861              2           VITAMIN WTR TROP MNGO 20OZ                                                                           851             7                 Pkg Beverages                                      NULL                                                                                                 NULL                                                                                                 NULL                                                                                                 NULL                                                                                                 Legacy                                                                                               S            1.0000                                  2.99"



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