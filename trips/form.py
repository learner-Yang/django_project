from  django  import  forms
from  .models  import  Article ,  BlogComment


class  BlogCommentForm ( forms . ModelForm ):
    class  Meta :
        """指定一些Meta選項以改變form被渲染後的樣式"""
        model  =  BlogComment  # form關聯的Model

        fields  =  [ 'user_name' ,  'user_email' ,  'body' ]
        # fields表示需要渲染的字段，這裡需要渲染user_name、user_email、body
        #這樣渲染後表單會有三個文本輸入框，分別是輸入user_name、user_email、 body的輸入框

        widgets  =  {
            #為各個需要渲染的字段指定渲染成什麼html組件，主要是為了添加css樣式。
            #例如user_name渲染後的html組件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            'user_name' :  forms . TextInput ( attrs = {
                'class' :  'form-control' ,
                'placeholder' :  "請輸入暱稱" ,
                'aria-describedby' :  "sizing-addon1" ,
            }),
            'user_email' :  forms . TextInput ( attrs = {
                'class' :  'form-control' ,
                'placeholder' :  "請輸入郵箱" ,
                'aria-describedby' :  "sizing-addon1" ,
            }),
            'body' :  forms. Textarea ( attrs = { 'placeholder' :  '我來評兩句~' }),
        }