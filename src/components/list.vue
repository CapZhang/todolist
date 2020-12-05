<template >
  <section>
    <ul class="todo-list" v-show="todoList.length">
      <li
        class="todo-item"
        v-for="(item, index) in todoList"
        v-bind:key="index + item.name"
      >
        <span>{{ index + 1 }}.</span>
        <p>
          <span></span>
          {{ item.name }}<br /><span class="todo-time" v-if="item.deadline"
            >截止时间: {{ chGMT(item.deadline) }}</span
          >
        </p>
        <button>开始</button>
        <button @click="removeItem(index)">完成</button>
      </li>
    </ul>
    <div class="todo-nodata" v-show="!todoList.length">
      恭喜你完成所有内容，请继续添加！！
    </div>
  </section>
</template>

<script>
// 格林威治时间修饰
Date.prototype.format = function (format) {
  var o = {
    "M+": this.getMonth() + 1, //month
    "d+": this.getDate(), //day
    "h+": this.getHours(), //hour
    "m+": this.getMinutes(), //minute
    "s+": this.getSeconds(), //second
    "q+": Math.floor((this.getMonth() + 3) / 3), //quarter
    S: this.getMilliseconds(), //millisecond
  };
  if (/(y+)/.test(format))
    format = format.replace(
      RegExp.$1,
      (this.getFullYear() + "").substr(4 - RegExp.$1.length)
    );
  for (var k in o)
    if (new RegExp("(" + k + ")").test(format))
      format = format.replace(
        RegExp.$1,
        RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length)
      );
  return format;
};

export default {
  data() {
    return {
      chGMT(gmtDate) {
        let mydate = new Date(gmtDate);
        let now_date = new Date();
        // mydate.setHours(mydate.getHours() + 8);
        let init_date = mydate.format("yyyy-MM-dd hh:mm:ss");
        let print_date
        if (mydate.getFullYear() == now_date.getFullYear()){
          console.log(mydate.getDate() != now_date.getDate());
          if (mydate.getDate() == now_date.getDate()){
            print_date = "今天"+" "+ mydate.format("hh:mm:ss");
          }else if(mydate.getDate() == now_date.getDate()+1){
            print_date = "明天"+" "+ mydate.format("hh:mm:ss");
          }else if(mydate.getDate() == now_date.getDate()+2){
            print_date = "后天"+" "+ mydate.format("hh:mm:ss");
          }else{
            print_date = init_date;
          }
        }
        return print_date
      },
    };
  },
  computed: {
    todoList: function () {
      return this.$store.state.items;
    },
  },
  methods: {
    removeItem(index) {
      this.$store.dispatch("removeItem", index);
    },
  },
};
</script>