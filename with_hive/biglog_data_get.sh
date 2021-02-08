#!/bin/bash
# @ author zhaowenfeng
# @date 20210208
# @desc test

date_today=$1
source ~/.bash_profile
qe_jiuying -e "
SET mapred.job.name = 'zwf_test_${date_today}';
SET mapred.map.tasks = 5000;
SET mapred.reduce.tasks = 1000;
SET mapred.job.map.capacity = 3000;
SET mapred.job.reduce.capacity = 1000;
SET mapred.job.priority = HIGH;
ADD CACHEARCHIVE /home/work/python-2.7.11.tar.gz;
ADD FILE ./script.py;

SELECT TRANSFORM(param_1, param_2)
USING 'python-2.7.11.tar.gz/python-2.7.11/bin/python script.py'
AS (t1, t2)
FROM table
LATERAL VIEW explode(use_traces) lv AS k_8409
WHERE event_day = ${date_today}
" > ./Data/xxx.${date_today}



# TRANSFORM(event_day, event_hour, cuid, usertraces)
#            using 'sh transformScript_zwf.sh'
#            as (result string)
#
# python python3.6.tar.gz/python3.6/bin/python3 prepareTestCase_zwf.py 1>&2

