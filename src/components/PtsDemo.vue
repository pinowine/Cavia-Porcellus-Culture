<template>
<canvas ref="canvas" width="800" height="600"></canvas>
</template>

<script>
export default {
name: 'Canvas',
mounted() {
    const canvas = this.$refs.canvas;
    const ctx = canvas.getContext('2d');

    const circles = [
    { x: 150, y: 100, radius: 400,  lineDashOffset: '-offset', setLineDash: [6, 4], strokeStyle: 'rgba(0,0,0,0.4)'},
    { x: 400, y: 200, radius: 50, lineDashOffset: '-offset', setLineDash: [5, 3],strokeStyle: 'rgba(0,0,0,0.4)'},
    { x: 425, y: 235, radius: 20, lineDashOffset: '-offset', setLineDash: [0, 0],strokeStyle: 'rgba(0,0,0,0.4)'},
    { x: 500, y: 300, radius: 70,  lineDashOffset: '-offset', setLineDash: [0, 0], strokeStyle: 'rgba(0,0,0,0.4)'},
    { x: 560, y: 360, radius: 70,  lineDashOffset: '-offset', setLineDash: [0, 0], strokeStyle: 'rgba(0,0,0,0.4)'},
    { x: 575, y: 375, radius: 70,  lineDashOffset: '-offset', setLineDash: [0, 0], strokeStyle: 'rgba(0,0,0,0.4)'},
    { x: 60, y: 180, radius: 360,  lineDashOffset: '-offset', setLineDash: [0, 0], strokeStyle: 'rgba(0,0,0,0.4)'},
    { x: 500, y: -100, radius: 500,  lineDashOffset: '-offset', setLineDash: [0, 0], strokeStyle:' rgba(0,0,0,0.4)'},
    ];

    let offset = 0;

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        circles.forEach(circle => {
            ctx.beginPath();
            ctx.arc(circle.x, circle.y, circle.radius, 0, Math.PI * 2);
            ctx.closePath();
            ctx.setLineDash(circle.setLineDash);
            ctx.lineDashOffset = circle.lineDashOffset;
            ctx.stroke()
            ctx.strokeStyle = circle.strokeStyle
        });

        requestAnimationFrame(draw);
    }

    function march() {
        offset++;
        if (offset > 16) {
            offset = 0;
        }
        draw();
        setTimeout(march, 20);
    }

    march();


}
}
</script>

<style lang='scss' scoped>



</style>
