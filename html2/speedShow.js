
function speedisply(ele) {
	var myChart = echarts.init(document.getElementById(ele));

const startAngle = 300
const endAngle = -60
option = {
   backgroundColor: '#00081c',
   title: [
      {
         text: `{value|${startAngle}}\n{name|${'今日环测评分'}}`,
         left: 'center',
         bottom: '42%',
         textStyle: {
            rich: {
               value: {
                  fontSize: '50',
                  color: '#ffffff',
                  padding: [8, 0]
               },
               name: {
                  fontSize: '20',
                  color: '#ffffff'
               }
            }
         }
      }
   ],
   series: [
      {
         name: '最外层-刻度尺',
         type: 'gauge',
         radius: '75%',
         startAngle,
         endAngle,
         axisLine: {
            lineStyle: {
               color: [[1, '#16d6ea']],
               width: 1
            }
         },
         axisTick: {
            distance: -6,
            length: 7,
            lineStyle: {
               color: '#006a73'
            },
            splitNumber: 10
         },
         splitLine: {
            distance: -11,
            length: 14,
            lineStyle: {
               color: '#10a1b5',
               width: 1
            }
         },
         axisLabel: {
            show: false
         },
         pointer: {
            show: false
         }
      },
      {
         name: '内层带指针',
         type: 'gauge',
         radius: '72%',
         startAngle,
         endAngle,
         axisLine: {
            lineStyle: {
               color: [[1, '#053d50']],
               width: 40
            }
         },
         axisTick: {
            show: false
         },
         splitLine: {
            show: false
         },
         axisLabel: {
            show: false
         },
         detail: {
            show: false
         },
         pointer: {
            show: true,
            length: '76%',
            offsetCenter: [0, '-24%'],
            width: 6,
            icon: 'path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z',
            itemStyle: {
               color: {
                  type: 'linear',
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [
                     {
                        offset: 0,
                        color: '#07ffd6'
                     },
                     {
                        offset: 0.2,
                        color: '#07ffd6'
                     },
                     {
                        offset: 0.8,
                        color: '#002f3c'
                     },
                     {
                        offset: 1,
                        color: '#001829'
                     }
                  ]
               }
            }
         },
         progress: {
            show: true,
            width: 40,
            itemStyle: {
               color: {
                  type: 'linear',
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [
                     {
                        offset: 0,
                        color: '#07ffd6'
                     },
                     {
                        offset: 1,
                        color: '#5eff10'
                     }
                  ]
               }
            }
         },
         data: [
            {
               value: 90
            }
         ]
      },
      {
         name: '中心效果圆',
         type: 'gauge',
         radius: '44%',
         startAngle: 0,
         endAngle: 360,
         axisLine: {
            lineStyle: {
               color: [[1, '#0AFFE9']],
               width: 1
            }
         },
         axisTick: {
            show: false
         },
         splitLine: {
            show: false
         },
         axisLabel: {
            show: false
         },
         detail: {
            show: false
         },
         pointer: {
            show: false
         },
         progress: {
            show: true,
            width: 80,
            itemStyle: {
               color: {
                  type: 'radial',
                  x: 0.5,
                  y: 0.5,
                  r: 0.5,
                  colorStops: [
                     {
                        offset: 0,
                        color: 'rgb(0, 224, 205, 0)'
                     },
                     {
                        offset: 0.1,
                        color: 'rgb(0, 224, 205, 0)'
                     },
                     {
                        offset: 0.3,
                        color: 'rgb(0, 224, 205, 0)'
                     },
                     {
                        offset: 0.4,
                        color: 'rgb(0, 224, 205, 0.05)'
                     },
                     {
                        offset: 0.5,
                        color: 'rgb(0, 224, 205, 0.1)'
                     },
                     {
                        offset: 1,
                        color: 'rgb(0, 224, 205, 0.3)'
                     }
                  ]
               }
            }
         },
         data: [
            {
               value: 100
            }
         ]
      }
   ]
}


myChart.setOption(option);

}