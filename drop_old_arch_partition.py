#!/usr/bin/python2.7
#Add comment
#Add new line once more
#Add line on my local comp
#Add line on my Remote Site comp
#Add something else
#Add blank row on the top
#Add once more blank row on the top
import pyodbc
import datetime
import re
import sys
import os
import optparse
#Switched to branch 'MyDev'

#bla bla bla at Dev Local Edit bla bla

#bla bla bla at Dev Remote Edit bla bla
#Add try to get with help FETCH

#Add blank row ALMOST on the top on the local comp. I try correct in the same row on LOCAL COMP
parser = optparse.OptionParser()
parser.add_option("-D", "--database", help="database name")
parser.add_option("-U", "--user",     help="database user")
parser.add_option("-W", "--password", help="database password")
parser.add_option("-P", "--port",     help="port to connect. use ndwh02 - 5433 ; ndwh02ufins - 6433", type="int")
(options, args) = parser.parse_args()

if not options.database or not options.port or not options.password or not options.user:
    parser.print_help()
    exit(1)

con_name = 'DSN=VerticaDB1'

cnxn   = pyodbc.connect(con_name)
cursor = cnxn.cursor()
start  = datetime.datetime.today()
print "time start: " + str(start)

# user_privilege
cursor.execute("SELECT 'DROP_PARTITION(''' || t.projection_schema || '.' || t.anchor_table_name || ''', ' || p.partition_key || ', false, true)' drop_part \
                  FROM partitions p \
                 INNER JOIN projections t ON p.projection_id = t.projection_id \
                 JOIN stg_owner.list_arch_table lt ON UPPER(t.anchor_table_name) = UPPER(lt.table_name) AND UPPER(p.table_schema) = UPPER(lt.schema_name) \
                 WHERE p.partition_key <= MONTH(add_months(sysdate,-3)) \
                 GROUP BY 1 \
                 ORDER BY 1")
table_list = cursor.fetchall()

for row in table_list:
    query = 'vsql -d %s -p %s -U %s -w %s -c %s' % (options.database, options.port, options.user, options.password, row.drop_part)
    os.system(query)
    #print query
