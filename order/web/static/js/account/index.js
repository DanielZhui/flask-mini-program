;
var account_index_ops = {
    init:function() {
        this.eventBind();
    },
    eventBind:function() {
        var that = this;
        $(".wrap_search .search").click(function() {
            // 在当前页面提交参数 eg: ?status=-1&mix_kw=ceshi&p=1
            $(".wrap_search").submit();
        });
    }
}

$(document).ready(function() {
    account_index_ops.init();
});