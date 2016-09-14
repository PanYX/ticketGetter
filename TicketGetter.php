<?php
$url = 'https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2016-09-28&leftTicketDTO.from_station=RTQ&leftTicketDTO.to_station=MDQ&purpose_codes=ADULT';
//$url = 'http://www.baidu.com';

function httpGet($url) {
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_TIMEOUT, 500);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
    curl_setopt($curl, CURLOPT_URL, $url);

    $res = curl_exec($curl);
    curl_close($curl);
    return $res;
}

return httpGet($url);



