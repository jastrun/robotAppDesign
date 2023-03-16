var myChart = echarts.init(document.getElementById('main'),'dark');


var speed=80;
option = {
    backgroundColor: '#f0f2f5',
    title: {
        text: '仪表盘'
    },
    series: [
        {
            name: '内圈小',
            type: 'gauge',

            pointer:{
              show:false
            },
            radius: '70%',
            startAngle: 200,
            endAngle: -20,
            splitNumber: 4,
            axisLine: { // 坐标轴线
                lineStyle: { // 属性lineStyle控制线条样式
                    color: [
                        [1, '#bfcbd9']
                    ],
                    width: 20
                }

            },
            splitLine: { //分隔线样式
                show: false,
            },
            axisLabel: { //刻度标签
                show: false,
            },
            axisTick: { //刻度样式
                show: false,
            },
            detail: {
                // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: 'bolder',
                fontSize:40,
                offsetCenter:[0, '20%']
            },
            data: [{
                value: speed,
                name: ''
            }]
        }, {
            name: '内圈小',
            type: 'gauge',
            title : {
                // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: 'bolder',
                fontSize: 30,
                fontStyle: 'italic',
                 offsetCenter: [0, '33%'],
            },
            pointer:{
              show:true
            },
            radius: '70%',
            startAngle: 200,
            endAngle: 50,
            splitNumber: 4,
            axisLine: { // 坐标轴线
                lineStyle: { // 属性lineStyle控制线条样式
                    color: [
                        [1, '#0093ee']
                    ],
                    width: 20,
                    shadowColor: '#0093ee', //默认透明
                    shadowOffsetX: 0,
                    shadowOffsetY: 0,
                    shadowBlur: 40,
                    opacity: 1,
                }

            },
            splitLine: { //分隔线样式
                show: false,
            },
            axisLabel: { //刻度标签
                show: false,
            },
            axisTick: { //刻度样式
                show: false,
            },
            detail: {
                // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: 'bolder',
                fontSize:40,
                offsetCenter:[0, '20%']
            },
            data: [{
                value: '120',
                name: 'km/h'
            }]
        },

    ]
};
myChart.setOption(option);