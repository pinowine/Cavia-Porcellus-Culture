<template>
    <div id="chart">
        <apexchart 
            type="bubble" 
            height="350" 
            :options="bubbleOptions" 
            :series="bubbleSeries">
        </apexchart>
    </div>
</template>
  
<script>
import VueApexCharts from 'vue3-apexcharts'

export default {
    components: {
        apexchart: VueApexCharts,
    },
    methods: {
        generateData(startDate, numEntries, min, max) {
        const data = [];
        const dateIncrement = 3 * 7 * 24 * 60 * 60 * 1000; 

        for (let i = 0; i < numEntries; i++) {
            const currentDate = new Date(startDate + (i * dateIncrement)).getTime();
            const entry = [currentDate, this.getRandomValue(min, max), this.getRandomValue(min, max)];
            data.push(entry);
        }
        console.log(data);

        return data;
        },
        getRandomValue(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
        }
    },
    data: function() {
        return {
            bubbleOptions: {
                chart: {
                height: 350,
                type: 'bubble',
                },
                colors: ['#5C4742', '#546E7A', '#2B908F', '#FD6A6A'],
                dataLabels: {
                    enabled: false
                },
                fill: {
                    opacity: 0.8
                },
                title: {
                    text: 'Contribution Gallery'
                },
                xaxis: {
                    tickAmount: 10,
                    type: 'datetime',
                    labels: {
                        datetimeFormatter: {
                            year: 'yyyy',
                            month: 'MM/yyyy',
                            day: 'MM/yyyy',
                            hour: 'HH:mm'
                    }
                    }
                },
                yaxis: {
                    max: 100
                }
            },
            bubbleSeries: [{
                name: 'Calvin!',
                data: this.generateData(new Date('11 Feb 2023 GMT').getTime(), 20, 1, 60)
                
            },
            {
                name: 'THisGMAT',
                data: this.generateData(new Date('20 Dec 2023 GMT').getTime(), 15, 5, 90)
            },
            {
                name: 'WHY?',
                data: this.generateData(new Date('5 Jan 2023 GMT').getTime(), 10, 10, 80)
            },
            {
                name: 'Herrobine',
                data: this.generateData(new Date('30 Jun 2023 GMT').getTime(), 8, 50, 100)
            }],
        };
    }

}


</script>

<style lang="scss" scoped>

#chart {
    margin-left: 10px;
}
</style>