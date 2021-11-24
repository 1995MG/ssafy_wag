<template>
  <div class="articlelist container text-white">
    <!-- <b-table-simple class="table table-striped" :per-page="perPage" :current-page="page">
      <b-thead>
        <b-tr class="table-light">
          <b-th class="text-center" scope="col" style="width: 10%">번호</b-th>
          <b-th class="text-center" scope="col" style="width: 50%">제목</b-th>
          <b-th scope="col" style="width: 15%">작성자</b-th>
          <b-th class="text-center" scope="col" style="width: 15%">작성일</b-th>
          <b-th class="text-center" scope="col" style="width: 10%">좋아요</b-th>
        </b-tr>
      </b-thead>  
      <b-tbody class="table-light">
        <article-list-item
          v-for="article in articles"
          :key="article.id"
          :article="article"
        >
        </article-list-item>
      </b-tbody>
    </b-table-simple> -->
    <div style="height: 700px">
      <b-table class="table-light table-striped" id="my-table" :items="articles" :fields="fields" :per-page="perPage" :current-page="page" @row-clicked="toDetail"></b-table>
    </div>
    <div class="d-flex justify-content-center">
      <b-pagination @change="onPageChanged" :total-rows="totalRows" :per-page="perPage" v-model="page" class="my-0"></b-pagination>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import ArticleListItem from '@/components/ArticleListItem.vue'

export default {
  name: 'ArticleList',
  data: function () {
    return {
      // fields: ['Id', ],
      fields: [{
          key: 'id',
          label: '번호',
          thClass: 'w10, text-center',
          tdClass: 'text-center',
        },
        {
          key: 'title',
          label: '제목',
          thClass: 'w50 text-center',
          tdClass: 'px-5',
        },
        {
          key: 'username',
          label: '작성자',
          thClass: 'w15'
        },
        {
          key: 'created_at',
          label: '작성일',
          thClass: 'w15 text-center',
          tdClass: 'text-center',
        },
        {
          key: 'like_users.length',
          label: '좋아요',
          thClass: 'w10 text-center',
          tdClass: 'text-center',
        }
      ],
      articleList: null,
      totalRows: null,
      perPage: 15,
      page: 1,
    }
  },
  components: {
    // ArticleListItem,
  },
  props: {
    articles: Array,
  },
  methods: {
    toDetail: function (item) {   
        this.$router.push({ name: 'ArticleDetail', params: {articleId: item.id} })   
    },
    onPageChanged(page){
      this.$router.push({
        path: '/community',
        query:{page:page}
      })
    },
  },
  mounted() { 
    axios.get('http://127.0.0.1:8000/community/') // 프로젝트의 개수를 가져오기
    .then(response => {
        this.totalRows=response.data.length
    });
    console.log("query:"+this.$route.query.page)
  },
  created: function () {
  }
}
</script>

<style>

</style>