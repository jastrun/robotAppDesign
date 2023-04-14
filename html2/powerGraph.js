
function energyDisply1(ele) {
	var myChart = echarts.init(document.getElementById(ele));

function randomData() {
  value = Math.random() * 5;
  return value;
}
let data = [];
let timex = [];
let value = Math.random() * 0.1;
for (var i = 0; i < 30; i++) {
  data.push(randomData());
  timex.push(i);
}
let colorArr = ['#0000FF', '#00FF00', '#FFF100', '#E60012', '#FF00FF'];
let textArr = ['Ⅰ类', 'Ⅱ类', 'Ⅲ类', 'Ⅳ类', 'Ⅴ类'];
let valuetArr = [1, 2, 3, 4, 5];
let jczArr = [1, 1.3, 1.3, 4, 2, 1.4, 3];
let newArr = [];
function dealLine(num) {
  let back = [];
  for (var i = 0; i < 61; i++) {
    back.push(num);
  }
  return back;
}
for (var i = 0; i < 10; i++) {
  if (textArr[i]) {
    debugger;
    newArr.push({
      name: textArr[i],
      type: 'line',
      showAllSymbol: true,
      showSymbol: false,
      symbol: 'circle',
      symbolSize: 4,
      lineStyle: {
        normal: {
          width: 2,
          color: colorArr[i] // 线条颜色
        },
        type: 'solid'
      },
      itemStyle: {
        color: colorArr[i],
        borderWidth: 2,
        borderColor: '#fff'
      },

      tooltip: {
        show: true
      },
      data: dealLine(valuetArr[i])
    });
  }
}
option = {
  backgroundColor: '#11283a',
  tooltip: {
    trigger: 'axis'
  },
  layout: {
        padding: {
          left: 10,
          right: 10,
          top: 10,
          bottom: 10
        }
      },
  color: ['#fcba62', '#69f0ff'],
  legend: {
    top: '8%',
    right: '5%',
    textStyle: {
      color: '#fff',
      fontSize: 14,
      padding: [0, 8, 0, 8]
    }
  },
  grid: {
    top: '15%',
    left: '10%',
    right: '5%',
    bottom: '15%'
  },
  xAxis: [
    {
      type: 'category',
      axisLine: {
        lineStyle: {
          color: '#494e54'
        }
      },
      axisLabel: {
        color: '#d9d9d9'
      },
      splitLine: {
        show: false
      },
      boundaryGap: false,
      data: timex //this.$moment(data.times).format("HH-mm") ,
    }
  ],

  yAxis: [
    {
      type: 'value',
      // max:20,
      name: '单位：m/s',
      nameTextStyle: {
        color: '#fff',
        fontSize: 12
      },
      axisLine: {
        lineStyle: {
          color: '#494e54',
          fontSize: 14
        }
      },
      splitLine: {
        show: false
      },
      axisLabel: {
        show: true,
        textStyle: {
          color: '#d9d9d9'
        }
      }
    }
  ],
  series: [
    {
      name: '监测值',
      type: 'line',
      showAllSymbol: true,
      showSymbol: false,
      symbol: 'circle',
      symbolSize: 7,
      data: jczArr,
      smooth: true,
      itemStyle: {
        borderWidth: 2,
        color: 'rgba(43,254,192, 1)',
        borderColor: '#fff',
        normal: {
          lineStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: 'rgba(43,254,192, 1)'
              },
              {
                offset: 0.5,
                color: 'rgba(43,254,192, 0.7)'
              },
              {
                offset: 1,
                color: 'rgba(43,254,192,0)'
              }
            ])
          },
          areaStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: 'rgba(43,254,192, 0.9)'
              },
              {
                offset: 0.4,
                color: 'rgba(43,254,192, 0.5)'
              },
              {
                offset: 1,
                color: 'rgba(43,254,192, 0)'
              }
            ])
          }
        }
      }
    },
    ...newArr
  ]
};
setInterval(function () {
  for (var i = 0; i < 1; i++) {
    data.shift();
    data.push(randomData());
  }
  myChart.setOption({
    series: [
      {
        data: data
      }
    ]
  });
}, 1000);


myChart.setOption(option);

}