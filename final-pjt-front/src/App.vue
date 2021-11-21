<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ name: 'Home' }">홈</router-link> |
      <router-link :to="{ name: 'Recommend' }">영화추천</router-link> |
      <router-link :to="{ name: 'Community' }">커뮤니티</router-link> |
      <span v-if="isSignin">
        <router-link :to="{ name: 'Profile' }">프로필</router-link> |
        <router-link to="#" @click.native="logout">로그아웃</router-link> |
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">회원가입</router-link> |
        <router-link :to="{ name: 'Signin' }">로그인</router-link> |
      </span>
    </div>
    <router-view @login="isSignin=true"/>
  </div>
</template>

<script>
import jwt_decode from 'jwt-decode'

export default{
  name: 'App',
  data: function() {
    return {
      isSignin: false,
      username: null,
    }
  },
  methods: {
    logout: function () {
      this.isSignin = false,
      localStorage.removeItem('jwt')
      this.$router.push({ name:'Signin' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    const decodedToken = jwt_decode(token)
    this.username = decodedToken.username

    if (token) {
      this.isSignin = true
    }
  },
  updated: function () {
    const token = localStorage.getItem('jwt')
    const decodedToken = jwt_decode(token)
    this.username = decodedToken.username

    if (token) {
      this.isSignin = true
    }
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>