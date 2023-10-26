<template>
    <div id="radialChart">
        <apexchart
            height="300"
            type="radialBar"
            :options="radialOptions"
            :series="radialSeries"
        ></apexchart>
    </div>
</template>
  
<script>
import VueApexCharts from 'vue3-apexcharts'

export default {
    components: {
        apexchart: VueApexCharts,
    },
    data: function() {
        return {
            radialOptions: {
                chart: {
                    id: "RadialBar",
                },
                plotOptions: {
                    radialBar: {
                        offsetX: -60,
                        offsetY: 0,
                        startAngle: 0,
                        endAngle: 270,
                        hollow: {
                            margin: 5,
                            size: '30%',
                            background: 'transparent',
                            image: undefined,
                        },
                        track: {
                            dropShadow: {
                            enabled: true,
                            top: 3,
                            left: 2,
                            blur: 2,
                            opacity: 0.10
                            }
                        },
                        dataLabels: {
                        name: {
                            show: false,
                        },
                        value: {
                            show: false,
                        }
                        }
                    },
                },
                colors: ['#5C4742', '#A5978B', '#8D5B4C', '#5A2A27'],
                labels: ['Hangzhou', 'Shanghai', 'Beijing', 'Guangzhou'],
                legend: {
                    show: true,
                    floating: true,
                    fontSize: '12px',
                    position: 'left',
                    offsetX: -15,
                    offsetY: 0,
                    labels: {
                        useSeriesColors: true,
                    },
                    markers: {
                        size: 0
                    },
                    formatter: function(seriesName, opts) {
                        return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
                    },
                    itemMargin: {
                        vertical: 0
                    }
                },
                responsive: [{
                    breakpoint: 480,
                    options: {
                        legend: {
                            show: false
                        }
                    }
                }]
            },
            radialSeries: [76, 67, 61, 90]
        };
    }

}


</script>

<style lang="scss" scoped>

</style>