$(window).load(function () {
    $(".loading").fadeOut()
})

/****/
$(document).ready(function () {
    var whei = $(window).width()
    $("html").css({fontSize: whei / 20})
    $(window).resize(function () {
        var whei = $(window).width()
        $("html").css({fontSize: whei / 20})
    });
});


$(window).load(function () {
    $(".loading").fadeOut()
})
$(function () {

    echarts_3()
    echarts_4()
    bt01()
    bt02()
    bt03()
    bt04()
    sycm2()

    function sycm2() {


        // 获取名为 'class' 的查询参数的值
        let className = returnParam("class");
        if (className == null || className === "undefined") {
            className = "all";
        }
        var dom = document.getElementById('sycm2');
        var myChart = echarts.init(dom, null, {
            renderer: 'canvas',
            useDirtyRect: false
        });
        var app = {};

        var option;

        option = {
            graphic: {
                elements: [
                    {
                        type: 'text',
                        left: 'center',
                        top: 'center',
                        style: {
                            text: className,
                            fontSize: 100,
                            fontWeight: 'bold',
                            lineDash: [0, 200],
                            lineDashOffset: 0,
                            fill: 'transparent',
                            stroke: '#1075dc',
                            lineWidth: 1
                        },
                        keyframeAnimation: {
                            duration: 3000,
                            loop: true,
                            keyframes: [
                                {
                                    percent: 0.7,
                                    style: {
                                        fill: 'transparent',
                                        lineDashOffset: 200,
                                        lineDash: [200, 0]
                                    }
                                },
                                {
                                    // Stop for a while.
                                    percent: 0.8,
                                    style: {
                                        fill: 'transparent'
                                    }
                                },
                                {
                                    percent: 1,
                                    style: {
                                        fill: '#1075dc'
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        };

        if (option && typeof option === 'object') {
            myChart.setOption(option);
        }

        window.addEventListener('resize', myChart.resize);

    }


    function echarts_4() {
        var myChart = echarts.init(document.getElementById('echart4'));
        option1 = {
             backgroundColor: 'rgba(14,93,211,0.08)',
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            legend: {
                data: ['java', 'python'],
                top: '5%',
                textStyle: {
                    color: "#fff",
                    fontSize: '12',

                },

                itemGap: 35
            },
            grid: {
                left: '0%',
                top: '40px',
                right: '0%',
                bottom: '0',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: ['1', '2', '3', '4', '5', '6', '7'],
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    rotate:50,
                    show: true,
                     splitNumber: 2,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [
                {
                    type: 'value',
                    axisLabel: {
                        // formatter: '{value} %',
                        show: true,
                        textStyle: {
                            color: "rgba(255,255,255,.6)",
                            fontSize: '12',
                        },
                    },
                    axisTick: {
                        show: false,
                    },
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: "rgba(255,255,255,.1	)",
                            width: 1,
                            type: "solid"
                        },
                    },
                    splitLine: {
                        lineStyle: {
                            color: "rgba(255,255,255,.1)",
                        }
                    }
                }],
            series: [

                {
                    name: 'java',
                    type: 'line',
                    smooth: true,
                    data: [100, 2, 6, 4, 5, 12, 20],
                    barWidth: '15',
                    barGap: 1,
                    itemStyle: {
                        normal: {
                            color: '#62c98d',
                            opacity: 1,
                            barBorderRadius: 5,
                        }
                    }
                },
                {
                    name: 'python',
                    type: 'line',
                    smooth: true,
                    data: [7, 11, 8, 13, 10, 13, 10],

                    itemStyle: {
                        normal: {
                            color: '#ffc000',
                            opacity: 1,

                            barBorderRadius: 5,
                        }
                    }
                }
            ]
        };



        myChart.setOption(option1);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
        $(".sebtn a").click(function () {
            $(this).addClass("active").siblings().removeClass("active")
        })
        $(".sebtn a").eq(0).click(function () {
            myChart.setOption(option1);
        })
        $(".sebtn a").eq(1).click(function () {
            myChart.setOption(option2);
        })
        $(".sebtn a").eq(2).click(function () {
            myChart.setOption(option3);
        })

    }

    function echarts_3() {
        var myChart = echarts.init(document.getElementById('echart3'));
        var spNum = 5, _max = 100;
        var legendData = ['已完成', '未完成'];
        var y_data = ['字段名称1', '字段名称2', '字段名称3', '字段名称4'];

        var data1 = [10, 15, 100, 13];
        var data2 = [19, 50, 40, 33];

        var fomatter_fn = function (v) {
            return (v.value / _max * 100).toFixed(0)
        }
        var _label = {
            normal: {
                show: true,
                position: 'inside',
                formatter: fomatter_fn,
                textStyle: {
                    color: '#fff',
                    fontSize: 12
                }
            }
        };
        option = {

            grid: {
                containLabel: true,
                top: 10,
                left: 0,
                right: 15,
                bottom: -10
            },
            tooltip: {
                show: true,
                formatter: '{b}<br/>{a}:{c}'
            },
            xAxis: {
                splitNumber: spNum,
                // interval: _max / spNum,
                //max: _max,
                axisLabel: {
                    show: false,
                    formatter: function (v) {
                        var _v = (v / _max * 100).toFixed(0);
                        return _v == 0 ? _v : _v + '%';
                    }
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }

            },
            yAxis: [{
                data: y_data,
                axisLabel: {
                    fontSize: 14,
                    color: 'rgba(255,255,255,.6)'

                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false
                }
            }, {
                show: false,
                data: y_data,
                axisLine: {
                    show: false
                }
            }],
            series: [{
                type: 'bar',
                name: '已完成',
                stack: '2',
                label: _label,
                legendHoverLink: false, barWidth: '50%',
                itemStyle: {
                    normal: {
                        color: '#58c485'
                    },
                    emphasis: {
                        color: '#58c485'
                    }
                },
                data: data1
            }, {
                type: 'bar',
                name: '未完成',
                stack: '2',
                legendHoverLink: false, barWidth: '50%',
                label: _label,
                itemStyle: {
                    normal: {
                        color: '#ea7231'
                    },
                    emphasis: {
                        color: '#ea7231'
                    }
                },
                data: data2
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function bt01() {
        var myChart = echarts.init(document.getElementById('bt01'));
        var data1 = 1//己完成
        var data2 = 18//未完成
        var data3 = data2 / (data1 + data2) * 100
        option = {
            title: [{
                text: data3.toFixed(1) + '%',
                x: 'center', y: '54%',
                textStyle: {
                    fontSize: 18,
                    fontWeight: 'bold',
                    fontStyle: 'normal',
                    color: '#fff'
                }
            }, {
                text: '本科以上',
                x: 'center', y: '68%',
                textStyle: {
                    fontSize: 10,
                    fontWeight: 'normal',
                    fontStyle: 'normal',
                    color: 'rgba(255,255,255,.6)'
                }

            }, {
                text: '学历要求',
                x: 'center', y: '20',
                textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#fff'
                }

            }],
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b}: {c} ({d}%)'
            },
            color: ['#58c485', '#ea7231'],
            series: [
                {
                    name: '要求',
                    type: 'pie', center: ['50%', '65%'], radius: ['45%', '60%'],
                    startAngle: 360,
                    avoidLabelOverlap: false,
                    label: {
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            show: false,
                            textStyle: {
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data: [{
                        value: data1,
                        name: '本科'
                    },
                        {
                            value: data2,
                            name: '专科'

                        },


                    ]

                }]

        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function bt02() {
        var myChart = echarts.init(document.getElementById('bt02'));
        var data1 = 14//己完成
        var data2 = 18//未完成
        var data3 = data1 / (data1 + data2) * 100
        option = {
            title: [{
                text: data3.toFixed(1) + '%',
                x: 'center', y: '54%',
                textStyle: {
                    fontSize: 18,
                    fontWeight: 'bold',
                    fontStyle: 'normal',
                    color: '#fff'
                }
            }, {
                text: '己完成',
                x: 'center', y: '68%',
                textStyle: {
                    fontSize: 10,
                    fontWeight: 'normal',
                    fontStyle: 'normal',
                    color: 'rgba(255,255,255,.6)'
                }

            }, {
                text: '字段名称1',
                x: 'center', y: '20',
                textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#fff'
                }

            }],
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b}: {c} ({d}%)'
            },
            color: ['#58c485', '#ea7231'],
            series: [
                {
                    name: '检点',
                    type: 'pie', center: ['50%', '65%'], radius: ['45%', '60%'],
                    startAngle: 360,
                    avoidLabelOverlap: false,
                    label: {
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            show: false,
                            textStyle: {
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data: [{
                        value: data1,
                        name: '己完成'
                    },
                        {
                            value: data2,
                            name: '未完成'

                        },


                    ]

                }]

        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function bt03() {
        var myChart = echarts.init(document.getElementById('bt03'));
        var data1 = 104//己完成
        var data2 = 108//未完成
        var data3 = data1 / (data1 + data2) * 100
        option = {
            title: [{
                text: data3.toFixed(1) + '%',
                x: 'center', y: '54%',
                textStyle: {
                    fontSize: 18,
                    fontWeight: 'bold',
                    fontStyle: 'normal',
                    color: '#fff'
                }
            },
                {
                    text: '己完成',
                    x: 'center', y: '68%',
                    textStyle: {
                        fontSize: 10,
                        fontWeight: 'normal',
                        fontStyle: 'normal',
                        color: 'rgba(255,255,255,.6)'
                    }

                }, {
                    text: '字段名称2',
                    x: 'center', y: '20',
                    textStyle: {
                        fontSize: 14,
                        fontWeight: 'bold',
                        color: '#fff'
                    }

                }],
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b}: {c} ({d}%)'
            },
            color: ['#58c485', '#ea7231'],
            series: [
                {
                    name: '检点',
                    type: 'pie', center: ['50%', '65%'], radius: ['45%', '60%'],
                    startAngle: 360,
                    avoidLabelOverlap: false,
                    label: {
                        show: false,

                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data: [
                        {
                            value: data1,
                            name: '己完成'

                        }, {
                            value: data2,
                            name: '未完成'
                        },
                    ]

                }]

        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function bt04() {
        var myChart = echarts.init(document.getElementById('bt04'));
        var data1 = 1000//己完成
        var data2 = 552//未完成
        var data3 = data1 / (data1 + data2) * 100
        option = {
            title: [{
                text: data3.toFixed(1) + '%',
                x: 'center', y: '54%',
                textStyle: {
                    fontSize: 18,
                    fontWeight: 'bold',
                    fontStyle: 'normal',
                    color: '#fff'
                }
            }, {
                text: '己完成',
                x: 'center', y: '68%',
                textStyle: {
                    fontSize: 10,
                    fontWeight: 'normal',
                    fontStyle: 'normal',
                    color: 'rgba(255,255,255,.6)'
                }

            }, {
                text: '字段名称3',
                x: 'center',
                y: '20',
                textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#fff'
                }

            }],
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b}: {c} ({d}%)'
            },
            color: ['#58c485', '#ea7231'],
            series: [
                {
                    name: '检点',
                    type: 'pie',
                    center: ['50%', '65%'], radius: ['45%', '60%'],
                    startAngle: 360,
                    avoidLabelOverlap: false,
                    label: {
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            show: false,
                            textStyle: {
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data: [{
                        value: data1,
                        name: '己完成'
                    },
                        {
                            value: data2,
                            name: '未完成'

                        },


                    ]

                }]

        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
})


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


// 获取下拉选择器元素
const selectElement = document.getElementById('fruit-select');
// 获取用于显示选择结果的元素
const selectedFruitElement = document.getElementById('selected-fruit');


// 当用户选择不同的选项时触发事件
selectElement.addEventListener('change', function () {
    const encodedParam = encodeURIComponent(selectElement.value);

    window.location.href = '/?class=' + encodedParam;
});



















