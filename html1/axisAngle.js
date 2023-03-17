function angleDisply(data,ele) {
var myChart = echarts.init(document.getElementById(ele));
angleData=data
option = {
   backgroundColor:' rgba(128, 128, 128, 0.3)',

   series: [
      //标题和数字部分
        {
            type: 'gauge',
            radius: '45%',
            center: ['50%', '60%'],
            min: 0,
            max: 360,
            splitNumber: 5,
            axisLine: {
                show: false,
                lineStyle: {
                    opacity: 0,
                },
            },
            axisLabel: {
                show: false,
            },
            pointer: {
                show: false,
            },
            axisTick: {
                show: false,
            },
            splitLine: {
                show: false,
            },
            detail: {
                color: '#fff',
                fontSize: 20,
                offsetCenter: [0, 15],
                fontWeight: 700,
            },
            title: {
                //标题
                offsetCenter: [20, 10],
                textStyle: {
                    fontSize: 24,
                    color: '#FFFFFF',
                },
            },
             data: [{
            value: data,
            name: '°',
        }],
        },




      {
        type: "pie",
        labelLine: {
          show: false,
        },
        z: 10,
        radius: 3,
        data: [
          {
            value: 100,
            itemStyle: {
              color: "#fff",
            },
          },
        ],
      },
      {
        name: "hour",
        type: "gauge",
        startAngle: 90,
        endAngle: -270,
        min: 0,
        max: 360,
        splitNumber: 8,
        radius: "70%",
        axisLine: {
          lineStyle: {
            width: 1,
            color: [[1, "rgba(34, 86, 186, 1)"]],
            shadowColor: "rgba(0, 0, 0, 0.5)",
            shadowBlur: 15,
          },
        },
        splitLine: {
          distance: 0,
          lineStyle: {
            shadowColor: "rgba(0, 0, 0, 0.3)",
            shadowBlur: 3,
            shadowOffsetX: 1,
            shadowOffsetY: 2,
            color: "#3379FC",
          },
        },
        axisLabel: {
          fontSize: 12,
          distance: -40,
          color: "#C0E5F9",
          formatter: function (value) {
            if (value === 360) {
              return "";
            }
            return value;
          },
        },
        axisTick: {
          distance: 0,
          lineStyle: {
            color: "#3379FC",
          },
          length: 6,
        },
        pointer: {
          show: true,
          length: "70%",
          width: "5",
          itemStyle: {
            color: "#007BF9",
          },
        },
        detail: {
          show: false,
        },
        data: [
          {
            value: angleData,
              name:ele,
          },

        ],
          title:{
                show: true,
                offsetCenter: [0, '-20%'], // x, y，单位px
                textStyle: {
                    color: '#7494ff',
                    fontSize: 20,
                },
            },
      },
    ]
};

myChart.setOption(option);
}