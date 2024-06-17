const Ip_Port = () => {
    let ip = window.location.hostname;
    let port = window.location.port;
    return ip + ":" + port;
}


const submitForm = (...objs) => {

    let v1 = document.getElementById("validationCustom01");//采集目的
    let v2 = document.getElementById("validationCustom02");//采集关键字
    let v3 = document.getElementById("validationCustom03");//采集页数
    let v4 = document.getElementById("validationCustom04");//采集城市
    let v5 = document.getElementById("validationCustom05");//采集目标

    let url;
    let domain_name;
    if (v5.value === "BOSS直聘") {
        url = `https://www.zhipin.com/web/geek/job?city=101110100&query=` + v2.value;
        domain_name = "www.zhipin.com";
    } else if (v5.value === "智联招聘") {
        url = `https://sou.zhaopin.com/?jl=854&kw=` + v2.value;
        domain_name = "sou.zhaopin.com";
    }

    const formData = new FormData();
    formData.append('domain_name', domain_name);
    formData.append('page_num', v3.value);
    formData.append('url', url);
    formData.append('Keyword', v2.value);


    axios.post(`${ipAddresses}/visualizeData`, formData)
        .then(response => {
            console.log('Response:', response.data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    // alert(111)

}



