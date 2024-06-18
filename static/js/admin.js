const Ip_Port = () => {
    let ip = window.location.hostname;
    let port = window.location.port;
    return ip + ":" + port;
}

//根据时间和随机数生成任务ID
function taskId() {
    const timestamp = new Date().getTime(); // 获取当前时间戳
    const randomNum = Math.floor(Math.random() * 1000); // 生成一个随机数

    const uniqueId = `${timestamp}_${randomNum}`; // 结合时间戳和随机数生成唯一ID

    return uniqueId;
}


const submitForm = (...objs) => {
    pxmu.toast({
        msg: '任务已提交', //内容 不能为空
        time: 2500, //停留时间 默认2500毫秒
        bg: 'rgb(16,117,220)', //背景颜色 默认黑色
        color: '#fff', //文字颜色 默认白色
        location: '',//居中center 顶部top 底部bottom默认
        animation: 'slidedown', //显示的动画 默认fade 动画支持详见动画文档
        type: 'wap', //默认wap样式 可选参数：pc 入参pc时
        status: '', //可选参数 success成功 warn警告 error错误 仅在type=pc时候生效，wap时可通过自定义bg、color改变样式
    });
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
        //https://sou.zhaopin.com/?jl=854&kw=%E8%85%BE%E8%AE%AF&p=2
        domain_name = "sou.zhaopin.com";
    }
    const TaskId = taskId();
    setCookie("taskId", TaskId, 1);
    const formData = new FormData();
    formData.append('domain_name', domain_name);
    formData.append('page_num', v3.value);
    formData.append('url', url);
    formData.append('Keyword', v2.value);
    formData.append('City', v4.value);
    formData.append('taskId', TaskId);
    formData.append('CollectionPurpose', v1.value);
    formData.append('CollectionTarget', v5.value);


    axios.post(`${ipAddresses}/visualizeData`, formData)
        .then(response => {
            console.log('Response:', response.data);
        })
        .catch(error => {
            console.error('Error:', error);
        });

}


function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days  * 60 * 60 * 1000)); // 设置cookie过期时间

    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}




