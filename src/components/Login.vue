<template>
    <div class="login-container">
        <div class="logintitle">LOGIN</div>
        <div class="login-main">
            <div class="user-container">
                <span class="user-icon">
                    <img src="../assets/img/user.svg" alt="">
                    UserID
                </span><br/>
                <label class="place-holder"></label>
                <input 
                type="text" 
                class="input"
                v-model="userValue"
                />
            </div>
            <div class="password-container">
                <span class="password-icon">
                    <img src="../assets/img/password.svg" alt="">
                    Password
                </span><br/>
                <label class="place-holder"></label>
                <input 
                type="text" 
                class="input"
                v-model="passwordValue"
                />
            </div>
            <button class="login-btn" @click="checkLogin(userValue,passwordValue)">LOGIN</button>
        </div>
        <button class="register-btn" @click="register">
            <img src="../assets/img/register.svg" alt=""><br/>
            REGISTER
        </button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            userValue: '',
            passwordValue: '',
        }
    },
    methods: {
        checkLogin(user,password) {
            if(user == 'Escotom' && password == '3620572020') {
                this.$router.push('/inner')
            } else {
                alert('Wrong username or password, please retry or register.')
            }
        },
        register() {
            alert('We need a summary of a same thing.')
        }
    },
}

</script>

<style lang="scss" scoped>
.login-container {
    width: 250px;
    border-radius: 5px;
    border: 2px solid #000000;
    padding: 10px;
    background-color: #F4F4F4;

    .logintitle {
        font-size: 30px;
        font-weight: bold;
        padding-top:30px;
        padding-bottom: 30px;
        border-bottom: 2px solid #797979;
        text-align: center;
    }

    .login-main {
        padding-top: 20px;
        padding-bottom: 20px;
        border-bottom: 2px solid #AAA;
        
        span {
            font-size: 15px;
        }

        input {
            padding-left: 3%;
            font-size: 15px;
            font-weight: lighter;
            color: #AAA;
            margin-top: 10px;
            width: 97%;
            height: 30px;
            border-radius: 6px;
            border: 1px solid #AAA;
            background: #FFF;
        }

        .user-container {
            margin-bottom: 20px;

        }

        .password-container {
            margin-bottom: 20px;
        }

        .login-btn {
            font-weight: bold;
            height: 40px;
            width: 40%;
            margin-left: 30%;
            margin-right: 30%;
            background-color: #FFF;
            border-radius: 6px;
            border:1px solid #AAA;
            box-shadow: 1px 0px 4px 0px rgba(0, 0, 0, 0.25);

            &:hover {
                background-color: #d4d4d4;
                transition: all 0.3s ease-in-out;
            }
        }
    }

    .register-btn {
        font-weight: bold;
        width: 60%;
        margin-top: 20px;
        margin-bottom: 20px;
        margin-left: 20%;
        margin-right: 20%;
        border-radius: 6px;
        border: 1px solid #AAA;
        background: #FFF;
        box-shadow: 1px 0px 4px 0px rgba(0, 0, 0, 0.25);
        padding-top: 5px;
        padding-bottom: 5px;

        &:hover {
            background-color: #d4d4d4;
            transition: all 0.3s ease-in-out;
        }

    }
}
</style>