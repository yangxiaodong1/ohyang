# 硬件测试报告
- 时间
    - 2017-9-27 18:25:00以前
- 数据表
    - test_device
- 总量（select count(*) from test_device where created_at < '2017-9-27 10:25:00';）
    - 15203
- 用户数量（select count(distinct(user_id)) from test_device where created_at < '2017-9-27 10:25:00';)
    - 7
- 设备数量（select count(distinct(identity_id)) from test_device where created_at < '2017-9-27 10:25:00';)
    - 9
- 按用户统计（select user_id, count(*) from test_device where created_at < '2017-9-27 10:25:00' group by user_id;）
    - |       1 |     2340 |
    - |       2 |     2234 |
    - |       4 |     3885 |
    - |       5 |     2292 |
    - |       6 |     1529 |
    - |       7 |     1703 |
    - |       8 |     1220 |


- 按设备统计（select identity_id,  count(*) from test_device where created_at < '2017-9-27 10:25:00' group by identity_id;）
    - | 0000000003  |      802 |
    - | 0000000005  |     1755 |
    - | 0000000006  |     2465 |
    - | 0000000007  |      989 |
    - | 0000000009  |     1268 |
    - | 000000000c  |     3486 |
    - | 000000000f  |     2979 |
    - | ff00f008ff  |     1449 |
    - | ff00f009ff  |       10 |



- 按用户和设备统计（select user_id, identity_id,  count(*) from test_device where created_at < '2017-9-27 10:25:00' group by user_id, identity_id;）
    - |       1 | 0000000003  |      182 |
    - |       1 | 0000000005  |      411 |
    - |       1 | 0000000007  |      225 |
    - |       1 | 0000000009  |      255 |
    - |       1 | 000000000c  |      579 |
    - |       1 | 000000000f  |      670 |
    - |       1 | ff00f008ff  |       18 |
    - |       2 | 0000000003  |      118 |
    - |       2 | 0000000005  |      467 |
    - |       2 | 0000000006  |      469 |
    - |       2 | 0000000007  |        1 |
    - |       2 | 0000000009  |      220 |
    - |       2 | 000000000c  |      389 |
    - |       2 | 000000000f  |      432 |
    - |       2 | ff00f008ff  |      130 |
    - |       2 | ff00f009ff  |        8 |
    - |       4 | 0000000003  |      144 |
    - |       4 | 0000000006  |      600 |
    - |       4 | 0000000007  |      322 |
    - |       4 | 0000000009  |      220 |
    - |       4 | 000000000c  |      958 |
    - |       4 | 000000000f  |      884 |
    - |       4 | ff00f008ff  |      757 |
    - |       5 | 0000000003  |      186 |
    - |       5 | 0000000005  |      263 |
    - |       5 | 0000000006  |      577 |
    - |       5 | 0000000007  |      118 |
    - |       5 | 0000000009  |      265 |
    - |       5 | 000000000c  |      769 |
    - |       5 | ff00f008ff  |      114 |
    - |       6 | 0000000003  |       32 |
    - |       6 | 0000000005  |      249 |
    - |       6 | 0000000006  |      281 |
    - |       6 | 0000000007  |      112 |
    - |       6 | 0000000009  |      142 |
    - |       6 | 000000000c  |      274 |
    - |       6 | 000000000f  |      416 |
    - |       6 | ff00f008ff  |       23 |
    - |       7 | 0000000003  |      140 |
    - |       7 | 0000000005  |      204 |
    - |       7 | 0000000006  |      301 |
    - |       7 | 0000000007  |      132 |
    - |       7 | 000000000c  |      319 |
    - |       7 | 000000000f  |      330 |
    - |       7 | ff00f008ff  |      276 |
    - |       7 | ff00f009ff  |        1 |
    - |       8 | 0000000005  |      161 |
    - |       8 | 0000000006  |      237 |
    - |       8 | 0000000007  |       79 |
    - |       8 | 0000000009  |      166 |
    - |       8 | 000000000c  |      198 |
    - |       8 | 000000000f  |      247 |
    - |       8 | ff00f008ff  |      131 |
    - |       8 | ff00f009ff  |        1 |

- 按设备和用户统计（select user_id, identity_id,  count(*) from test_device where created_at < '2017-9-27 10:25:00' group by identity_id, user_id;）
    - |       1 | 0000000003  |      182 |
    - |       2 | 0000000003  |      118 |
    - |       4 | 0000000003  |      144 |
    - |       5 | 0000000003  |      186 |
    - |       6 | 0000000003  |       32 |
    - |       7 | 0000000003  |      140 |
    - |       1 | 0000000005  |      411 |
    - |       2 | 0000000005  |      467 |
    - |       5 | 0000000005  |      263 |
    - |       6 | 0000000005  |      249 |
    - |       7 | 0000000005  |      204 |
    - |       8 | 0000000005  |      161 |
    - |       2 | 0000000006  |      469 |
    - |       4 | 0000000006  |      600 |
    - |       5 | 0000000006  |      577 |
    - |       6 | 0000000006  |      281 |
    - |       7 | 0000000006  |      301 |
    - |       8 | 0000000006  |      237 |
    - |       1 | 0000000007  |      225 |
    - |       2 | 0000000007  |        1 |
    - |       4 | 0000000007  |      322 |
    - |       5 | 0000000007  |      118 |
    - |       6 | 0000000007  |      112 |
    - |       7 | 0000000007  |      132 |
    - |       8 | 0000000007  |       79 |
    - |       1 | 0000000009  |      255 |
    - |       2 | 0000000009  |      220 |
    - |       4 | 0000000009  |      220 |
    - |       5 | 0000000009  |      265 |
    - |       6 | 0000000009  |      142 |
    - |       8 | 0000000009  |      166 |
    - |       1 | 000000000c  |      579 |
    - |       2 | 000000000c  |      389 |
    - |       4 | 000000000c  |      958 |
    - |       5 | 000000000c  |      769 |
    - |       6 | 000000000c  |      274 |
    - |       7 | 000000000c  |      319 |
    - |       8 | 000000000c  |      198 |
    - |       1 | 000000000f  |      670 |
    - |       2 | 000000000f  |      432 |
    - |       4 | 000000000f  |      884 |
    - |       6 | 000000000f  |      416 |
    - |       7 | 000000000f  |      330 |
    - |       8 | 000000000f  |      247 |
    - |       1 | ff00f008ff  |       18 |
    - |       2 | ff00f008ff  |      130 |
    - |       4 | ff00f008ff  |      757 |
    - |       5 | ff00f008ff  |      114 |
    - |       6 | ff00f008ff  |       23 |
    - |       7 | ff00f008ff  |      276 |
    - |       8 | ff00f008ff  |      131 |
    - |       2 | ff00f009ff  |        8 |
    - |       7 | ff00f009ff  |        1 |
    - |       8 | ff00f009ff  |        1 |