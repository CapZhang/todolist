<template >
  <section class="todo-read">
    <div v-show="readStatusDoing">正在读取...</div>
    <div v-show="!readStatusDoing && is_hiden">读取完成</div>
    <!-- <button v-on:click="readJsonDoc">重载</button> -->
  </section>
</template>

<script>
export default {
  data() {
    return {
      readStatusDoing: true,
      is_hiden: true
    };
  },
  methods: {
    timer() {
      return setTimeout(() => {
        this.is_hiden = false;
      }, 2000);
    },
    readJsonDoc() {
      console.log("readJson");
      this.$https
        .get("/todo")
        .then((res)=>{
          this.readStatusDoing = false;
          if (res.data.code == 0){
            console.log("读DB",res.data);
          }else{
            console.log("读DB",res.data);
            this.$store.dispatch("readItems", res.data);
          }
        })
        .catch((err)=>{
          return err
        });
    },
  },
  created() {
    // mounted vue的生命周期钩子，组件加载后使用
    this.readJsonDoc()
  },
  watch: {
    readStatusDoing() {
      this.timer();
    },
  },
};
</script>

<style scoped>
</style>