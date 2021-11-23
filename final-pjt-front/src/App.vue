<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg d-flex" style="background-color: rgba(33, 37, 41, 0.8)">
      <div class="container-fluid justify-content-around">
        <div class="d-flex align-items-center">
          <router-link class="navbar-brand" to="/">
            <img src="./assets/logo.png" alt="" width="100" height="100" class="d-inline-block align-text-top">
          </router-link>
          <div class="navbar-nav fs-3 fw-bold">
            <router-link class="nav-link text-white" to="/movies/recommend">영화추천</router-link>
            <router-link class="nav-link text-white" to="/community">커뮤니티</router-link>
          </div>
        </div>
        <div class="navbar-nav fs-3 fw-bold" v-if="isSignin">
          <router-link class="nav-link text-white" to="/accounts/profile">프로필</router-link>
          <router-link class="nav-link text-white" to="#" @click.native="logout">로그아웃</router-link>
        </div>
        <div class="navbar-nav fs-3 fw-bold" v-else>
          <router-link class="nav-link text-white" to="/accounts/signin">로그인</router-link>
          <router-link class="nav-link text-white" to="/accounts/signup">회원가입</router-link>
        </div>
      </div>
    </nav>
    <router-view class="mt-5" @login="isSignin=true"/>
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