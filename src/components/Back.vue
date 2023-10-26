<template>
    <div class="back">
        <span>
            <slot></slot>
        </span><br>
        <hr>
        <router-link to='/'>
            <button>Back to Home</button>
        </router-link>
    </div>
</template>

<script>

export default {
name: 'Back',
}
</script>

<style lang="scss" scoped>
.back {
    padding-top: 200px;
    text-align: center;
    
    span {
        font-size: 60px;
        font-weight: 600;
    }

    button {
        font-weight: bold;
        height: 40px;
        width: 20%;
        margin-left: 30%;
        margin-right: 30%;
        margin-top: 40px;
        background-color: #FFF;
        border-radius: 6px;
        border:1px solid #AAA;
        box-shadow: 1px 0px 4px 0px rgba(0, 0, 0, 0.25);

        &:hover {
            background-color: #d4d4d4;
            transition: all 0.3s ease-in-out;
        }
    }

    hr {
        margin-top: 40px;
    }
}

</style>