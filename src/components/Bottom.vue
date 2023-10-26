<template>
    <div class="bottom-container">
        <div class="contact-container">
            <h2>Contact With Us</h2>
            <h4>Tel.</h4>
            <p>10202392033</p>
            <h4>Email.</h4>
            <p>102993919@gmail.com</p>
            <h4>Add.</h4>
            <p>Rd 712, 12</p>
        </div>

        <div class="tree-container">
            <div
              v-for="(item, index) in data"
              :key="index"
              class="tree-main-item"
            >
                <router-link to="/loginpage">
                    <h2>{{ item.title }}</h2>
                </router-link>
                <p
                  v-for="(subItem, index) in item.children"
                  :key="index"
                  class="tree-sub-item"
                >
                    <router-link to="/loginpage">
                        {{ subItem.title }}
                    </router-link>
                </p>
            </div>
        </div>
        
    </div>
    <div class="copyright">
        <p>©CaviaPorcellusCulture Co., Ltd.  All rights reserved.</p>
    </div>
</template>

<script>
import bottomData from '../data/bottom.js';
import {ref} from 'vue';

export default {
    name: 'Bottom',

    setup() {

        const data = ref(bottomData);

        return {data};
    }
}
</script>

<style lang="scss" scoped>

.bottom-container {
    margin-top: 150px;
    margin-bottom: 70px;
    width: 100%;
    height: 300px;
    border-top: 1px solid #000;
    border-bottom: 1px solid #000;
    background: #F4F4F4;
    display: flex;
    justify-content: space-between;

    h2 {
        font-size: 30px;
        text-shadow: 1px 1px 3px #00000039;
    }

    h4 {
        font-size: 15px;
    }

    p {
        font-size: 20px;
    }

    .contact-container {
        width: 25%;
        margin-top: 35px;
        margin-bottom: 35px;
        padding-left: 60px;
        border-right: 1px solid #000;
        display: flex;
        flex-direction: column;
        justify-content: space-between;

        h4 {
            text-decoration: underline;
        }
    }

    .tree-container {
        display: flex;
        justify-content: baseline;
        width: 75%;
        padding-left: 8%;

        .tree-main-item {
            display: flex;
            flex-direction: column;
            justify-content: baseline;
            width: 100%;
            margin-top: 35px;
            margin-bottom: 35px;

            a {
                color: #000;
                text-decoration: none;
            }

            h2 {
                margin-bottom: 40px;
            }

            .tree-sub-item {
                margin-bottom: 30px;

                a {
                    color: #000;
                    text-decoration: none;
                    transition: all 0.3s ease-in-out;

                    &:hover {
                        color: #767676;
                        font-size: 25px;
                        font-weight: bold;
                        transition: all 0.3s ease-in-out;
                    }
                }

            }
        }
    }
}

.copyright {
    text-align: center;
    margin-bottom: 30px;
}

</style>