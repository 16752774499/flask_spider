const Ip_Port  = () => {
    let ip = window.location.hostname;
    let port = window.location.port;
    return ip+":"+port;
}




const submitForm = (...objs) => {
    objs.forEach(obj => {
        console.log(obj.value)
    })
}



