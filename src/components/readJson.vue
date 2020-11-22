<template >
    <section class="todo-read">
        <div v-show="readStatusDoing">正在读取...</div>
        <div v-show="!readStatusDoing && is_hiden">读取完成</div>
    </section>
</template>

<script>


export default {
    data() {
        return {
            readStatusDoing: true,
            readitemsStr: ["123"],
            temp: [
                {"name":"吃饭j"},
                {"name":"睡觉j"}
            ],
            is_run: true,
            is_hiden: true
        }
    },
    methods: {
        hiden_ele() {
            this.is_hiden = false
        },
        timer() {
        return setTimeout(()=>{
          this.hiden_ele()
        },5000)
      }
    },
    mounted: function () {
        // mounted vue的生命周期钩子，组件加载后使用
        if (this.is_run === true){
            this.readStatusDoing = false
            this.$store.dispatch("readItems", this.temp)
            this.is_run = false
        }
    },
    watch:{
        readStatusDoing() {
            this.timer()
        }
    }
}
</script>

<style scoped>

</style>