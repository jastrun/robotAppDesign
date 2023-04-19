
var myChart_powerg = echarts.init(document.getElementById('powerg'));

function randomData() {
  value = Math.random() * 250;
  return value;
}
var data = [];
let timex = [];
let value = Math.random() * 0.1;
for (var i = 0; i < 30; i++) {
  data.push(randomData());
  timex.push(i);
}
let colorArr = ['#0000FF', '#00FF00', '#FFF100', '#E60012', '#FF00FF'];
let textArr = ['低', '中低', '中', '中高', '高'];
let valuetArr = [30, 60, 90, 120, 150];
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
option_powerg = {
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
    right: '10%',
    bottom: '15%',
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
      name: '单位：Kw',
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
let data_powerg

function setdata_powerg(data){
  data_powerg=data
}



setInterval(function () {
  for (var i = 0; i < 1; i++) {
    data.shift();
    data.push(data_powerg);
  }
  myChart_powerg.setOption({
    series: [
      {
        data: data
      }
    ]
  });
}, 1000);


myChart_powerg.setOption(option_powerg);


window.addEventListener('resize', function() {
    myChart_powerg.resize();
  });