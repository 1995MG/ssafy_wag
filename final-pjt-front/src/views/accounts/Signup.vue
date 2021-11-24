<template>
  <div class="signup container text-white">
    <h1 class="fw-bold">회원가입</h1>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="username">아이디</label>
      <br>
      <input v-model="credentials.username" class="form-control" type="text" id="username">
    </div>
    <ul v-if="credentials.username.length < 3">
      <li>아이디는 최소 3자 이상이어야 합니다.</li>
    </ul>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="password">비밀번호</label>
      <br>
      <input v-model="credentials.password" class="form-control" type="password" id="password">
    </div>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="passwordConfirmation">비밀번호 확인</label>
      <br>
      <input v-model="credentials.passwordConfirmation" class="form-control" type="password" id="passwordConfirmation">
    </div>
    <ul v-if="credentials.password.length < 8">
      <li>비밀번호는 최소 8자 이상이어야 합니다.</li>
    </ul>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="first_name">이름</label>
      <br>
      <input v-model="credentials.first_name" class="form-control" type="text" id="first_name">
    </div>
      <p v-if="err">* 양식에 맞게 작성했는지 다시 한번 확인해주세요.</p>
    <button @click="signup" class="btn btn-success btn-lg my-3">가입하기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function() {
    return {
      credentials: {
        username: '',
        password: ''
      },
      err: false
    }
  },
  methods: {
    signupErr: function () {
      this.err = true
    },
    signup: function () {
      if (this.credentials.username.length >= 3 & this.credentials.password.length >= 8) {
        console.log('여긴가')
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/accounts/signup/',
          data: this.credentials
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'Signin' })
          }) 
          .catch((err) => {
            console.log(err)
            this.signupErr()
          })
      } else {
        this.err =true
      }
    },
  },
}
</script>


<style>

</style>