/**
 * 分页相关的配置
 **/
const pagination = {
    // 分页方式：[client] 客户端分页，[server] 服务端分页
    sidePagination: "server",
    // 初始化加载第一页，默认第一页
    pageNumber: 1,
    // 每页的记录行数
    pageSize: 10,
    // 可供选择的每页的行数 - (亲测大于1000存在渲染问题)
    pageList: [5, 10, 25, 50, 100, 500],
    // 在上百页的情况下体验较好 - 能够显示首尾页
    paginationLoop: true,
    // 展示首尾页的最小页数
    paginationPagesBySide: 2
};

/**
 * 按钮相关配置
 **/
const button = {
    // 按钮的类
    buttonsClass: 'default',
    // 类名前缀
    buttonsPrefix: 'btn'
}

/**
 * 图标相关配置
 **/
const icon = {
    // 图标前缀
    iconsPrefix: 'mdi',
    // 图标大小
    iconSize: 'mini',
    // 图标的设置
    icons: {
        paginationSwitchDown: 'mdi-door-closed',
        paginationSwitchUp: 'mdi-door-open',
        refresh: 'mdi-refresh',
        toggleOff: 'mdi-toggle-switch-off',
        toggleOn: 'mdi-toggle-switch',
        columns: 'mdi-table-column-remove',
        detailOpen: 'mdi-plus',
        detailClose: 'mdi-minus',
        fullscreen: 'mdi-monitor-screenshot',
        search: 'mdi-table-search',
        clearSearch: 'mdi-trash-can-outline'
    }
};

/**
 * 表格相关的配置
 **/
const table = {
    classes: 'table table-bordered table-hover table-striped lyear-table',
    // 请求地址
    url: `${ipAddresses}returnJobsList`,
    // 唯一ID字段
    uniqueId: 'id',
    // 每行的唯一标识字段
    idField: 'id',
    // 是否启用点击选中行
    clickToSelect: true,
    // 是否显示详细视图和列表视图的切换按钮(clickToSelect同时设置为true时点击会报错)
    showToggle: true,
    // 请求得到的数据类型
    dataType: 'json',
    // 请求方法
    method: 'get',
    // 工具按钮容器
    toolbar: '#toolbar',
    // 是否分页
    pagination: true,
    // 是否显示所有的列
    showColumns: true,
    // 是否显示刷新按钮
    showRefresh: true,
    // 显示图标
    showButtonIcons: true,
    // 显示文本
    showButtonText: false,
    // 显示全屏
    showFullscreen: true,
    // 开关控制分页
    showPaginationSwitch: true,
    // 总数字段
    totalField: 'total',
    // 当字段为 undefined 显示
    undefinedText: '-',
    // 排序方式
    sortOrder: "asc",
    ...icon,
    ...pagination,
    ...button
};

/**
 * 用于演示的列信息
 **/
const columns = [{
    field: 'example',
    checkbox: true,
    // 列的宽度
    width: 5,
    // 宽度单位
    widthUnit: 'rem',


}, {
    field: 'id',
    title: '采集ID',
    // 使用[align]，[halign]和[valign]选项来设置列和它们的标题的对齐方式。
    // h表示横向，v标识垂直
    align: 'center',
    // 是否作为排序列
    sortable: true,
    // 当列名称与实际名称不一致时可用
    sortName: 'sortId',
    switchable: false,
    // 列的宽度
    width: 8,
    // 宽度单位
    widthUnit: 'rem'
}, {
    field: 'jobName',
    align: 'center',
    title: '岗位名称',
    titleTooltip: '岗位名称'
}, {
    field: 'jobQualification',
    align: 'center',
    title: '要求学历',
}, {
    field: 'jobPay',
    align: 'center',
    title: '薪资',
}, {
    field: 'jobEXP',
    align: 'center',
    title: '经验要求',
}, {
    field: 'jobCorporation',
    // 是否可视(默认 - true)
    visible: true,
    align: 'center',
    title: '公司'
}, {
    field: 'jobAddress',
    align: 'center',
    title: '公司地点'
}, {
    field: 'SearchKeyword',
    align: 'center',
    title: '分类'
}, {
    field: 'status',
    title: '状态',
    formatter: function (value, row, index) {
        var value = "";
        if (row.status === 'True') {
            value = '<span class="badge bg-success">查看过</span>';
        } else if (row.status === 'False') {
            value = '<span class="badge bg-secondary">未查看</span>';
        } else {
            value = '<span class="badge bg-secondary">未知</span>';
        }
        return value;
    }
}, {
    field: 'operate',
    title: '操作',
    formatter: btnGroup,  // 自定义方法
    events: {
        'click .edit-btn': function (event, value, row, index) {
            event.stopPropagation();
            viewData(row);//第一个操作方法

        },
        'click .del-btn': function (event, value, row, index) {
            event.stopPropagation();
            console.log(row)
            delData(row);//第二个操作方法
        }
    }
}];

// 自定义操作按钮
function btnGroup() {
    let html =
        '<a href="#!" class="btn btn-sm btn-default me-1 edit-btn" title="查看" data-bs-toggle="tooltip"><i class="mdi mdi-window-open"></i></a>' +
        '<a href="#!" class="btn btn-sm btn-default del-btn" title="删除" data-bs-toggle="tooltip"><i class="mdi mdi-window-close"></i></a>';
    return html;
}

// 操作方法 - 查看
function viewData(row) {

    clickLi(row.id);
    window.open(row.jobUrl, '_blank');
    // 在需要的时候调用开启定时器函数
    startTimer();
}

// 操作方法 - 删除
function delData(row) {
    delJob(row.id);
    startTimer(500);
}

$('table').bootstrapTable({
    ...table,
    // 自定义的查询参数
    queryParams: function (params) {
        return {
            // 每页数据量
            limit: params.limit,
            // sql语句起始索引
            offset: params.offset,
            page: (params.offset / params.limit) + 1,
            // 排序的列名
            sort: params.sort,
            // 排序方式 'asc' 'desc'
            sortOrder: params.order
        };
    },
    columns,
    onLoadSuccess: function (data) {
        $("[data-bs-toggle='tooltip']").tooltip();
    }
});

function delJob(Id) {
    const params = {
        jobId: Id
    };
    axios.get(`${ipAddresses}/delJob`, {params: params})
        .then(response => {
            console.log(response.data)
        })
        .catch(error => {
            // 请求失败时的处理
            console.error(error);
            throw error; // 抛出错误以便在调用方捕获
        });
}


function clickLi(Id) {
    const params = {
        id: Id
    };
    axios.get(`${ipAddresses}/changeStatus`, {params: params})
        .then(response => {
            console.log(response.data)
        })
        .catch(error => {
            // 请求失败时的处理
            console.error(error);
            throw error; // 抛出错误以便在调用方捕获
        });
}

function refreshTable() {
    $('#table').bootstrapTable('refresh');
}

// 定义定时器变量
let timer;

// 开启定时器任务
function startTimer(time = 5000) {
    timer = setInterval(function () {
        console.log(new Date().toLocaleString());
        refreshTable();
        stopTimer();
    }, time);
}

// 关闭定时器任务
function stopTimer() {
    clearInterval(timer);
}

const btnJson = document.getElementById("btn_json");
const btnXls = document.getElementById("btn_xls");
const btnApi = document.getElementById("btn_api");
// 导出json
// 添加点击事件监听器
btnJson.addEventListener('click', function () {
    handleButtonClick(1);
});

btnXls.addEventListener('click', function () {
    handleButtonClick(2);
});

btnApi.addEventListener('click', function () {
    handleButtonClick(3);
});


function handleButtonClick(buttonId) {
    const ids = getSelectedRow();
    if (ids.length === 0) {
        adminAlert("请选择导出的数据", "warn");
    } else {
        adminAlert("正在导出数据，请稍后", "success");
        getIdsData(ids).then(async response => {
            console.log(response.data);
            let userInput = prompt("保存文件名", "");
            if (userInput.length !== 0) {
                switch (buttonId) {
                    case 1:
                        await SaveJson(response.data, userInput);
                        break;
                    case 2:
                        // 导出xls
                        await SaveEcxel(response.data, userInput);
                        break;
                    case 3:
                        // 导出api
                        SaveJson(response.data, userInput, false);
                        let apiurl = `${ipAddresses}file/${userInput}`;
                        let res = await createApi(apiurl, userInput);
                        console.log(res);
                        if (res.data.code === "10000") {
                            adminAlert(`导出成功，请访问：${apiurl}`, "success");
                        } else {
                            adminAlert("导出失败", res.data.message);
                        }
                        break;
                    default:
                        break;
                }
            } else {
                adminAlert("请输入文件名", "warn");
            }
        }).catch(error => {
            console.log(error);
        });
    }
}


//获取选中数据id
function getSelectedRow() {
    let selectedElements = document.querySelectorAll('.selected');
    // 遍历获取到的元素列表
    let ids = [];
    selectedElements.forEach(function (element) {
        ids.push(element.getAttribute('data-uniqueid'));
    });
    return ids;
}

function adminAlert(msg, status) {
    pxmu.toast({
        msg: msg, //内容 不能为空
        time: 2500, //停留时间 默认2500毫秒
        bg: 'rgb(16,117,220)', //背景颜色 默认黑色
        color: '#fff', //文字颜色 默认白色
        location: 'center',//居中center 顶部top 底部bottom默认
        animation: 'slidedown', //显示的动画 默认fade 动画支持详见动画文档
        type: 'pc', //默认wap样式 可选参数：pc 入参pc时
        status: status, //可选参数 success成功 warn警告 error错误 仅在type=pc时候生效，wap时可通过自定义bg、color改变样式
    });
}

async function getIdsData(ids) {
    let formData = new FormData();
    formData.append("ids", ids);
    {
        console.log(formData);

    }
    // 发起POST请求
    try {
        return await axios.post(`${ipAddresses}/returnIdsData`, formData);
    } catch (e) {
        return e;
    }
}

function SaveJson(SendData, fileName, status = true) {
    // 本地保存
    let json = JSON.stringify(SendData);
    let blob = new Blob([json], {type: 'application/json'});
    let url = URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.href = url;
    if (fileName === "") {
        fileName = "data"
    }
    if (status) {
        a.download = fileName + '.json';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
    let fromData = {
        filename: fileName,
        data: json
    }
    //服务器保存
    axios({
        timeout: 0,
        method: 'post',
        url: `${ipAddresses}/saveJson`, // 替换为你的目标URL
        data: fromData,
        headers: {'Content-Type': 'multipart/form-data'}
    })
        .then(function (response) {
            console.log(response.data);
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
}

function SaveEcxel(table, tableName) {
    let tempData = [];
    const keyOrder = ["id", "jobName", "jobUrl", "jobPay", "jobAddress", "jobQualification", "jobEXP", "jobCorporation", "jobCorporationUrl", "jobCorporationBg1", "jobCorporationBg2", "addTime", "status", "SearchKeyword"];
    const tableHeads = keyOrder.filter(key => Object.keys(table[0]).includes(key));
    const tableData = table.map(item => keyOrder.map(key => item[key]));
    tempData.push(tableHeads);
    tableData.forEach(item => tempData.push(item));
    let wb = XLSX.utils.book_new();
    // 将数据转换为工作表
    let ws = XLSX.utils.aoa_to_sheet(tempData);
    ws['!cols'] = [];
    table.forEach(() => {
        ws['!cols'].push({wpx: 150});
    })
    // 将工作表添加到工作簿
    XLSX.utils.book_append_sheet(wb, ws, `${tableName}`);
    // 生成Excel的配置项
    let wbout = XLSX.write(wb, {bookType: 'xlsx', type: 'binary'});


    // 创建下载链接
    let blob = new Blob([s2ab(wbout)], {type: 'application/octet-stream'});
    let url = URL.createObjectURL(blob);

    // 创建a标签并模拟点击下载
    let a = document.createElement('a');
    a.href = url;
    a.download = tableName + '.xlsx';
    document.body.appendChild(a);
    a.click();
    // 清理
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    let formData = new FormData();
    formData.append('file', blob);
    formData.append('fileName', tableName);
    axios({
        timeout: 0,
        method: 'post',
        url: `${ipAddresses}/saveExcel`, // 替换为你的目标URL
        data: formData,
        headers: {'Content-Type': 'multipart/form-data'}
    })
        .then(function (response) {
            console.log(response.data);
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
}


function s2ab(s) {
    let buf = new ArrayBuffer(s.length);
    let view = new Uint8Array(buf);
    for (let i = 0; i !== s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF;
    return buf;
}

async function createApi(apiurl, userInput) {
    let formData = new FormData();
    formData.append('url', apiurl);
    formData.append('name', userInput);
    return axios({
        method: 'post',
        url: `${ipAddresses}/createApi`,
        data: formData,
        headers: {'Content-Type': 'multipart/form-data'}
    })
}