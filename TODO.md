* 对环境变量的依赖
    - 很多插件需要一些vim之外的程序的帮助，比如tag文件，或者和其他程序相互交互，这时需要能够检测到系统中有没有安装某软件，安装什么版本
   outer package depend is not meet
        - maybe make some function for some big package system like debian's apt, redhat's yum.
    - 不少插件对与vim的版本，是否包含某种扩展，内部环境变量有要求，要求是否得到满足，甚至两个相互冲突脚本的如何检测
   inner env depend is not meet
        - maybe do a little to extend vim's function using python to meet this need
* 对其他package/plugin的依赖
    - 当前这种package数量还是非常少的，但随着需求变化和需求的增加，package之间必然出现相互依赖，甚至出现一些公共的库，这时依赖问题就出现了
   inner package depend is done
* 环境检测可以通过增加vim脚步完成,但是如何有效的自动解决环境依赖和实现环境依赖自动满足就是个大问题了
* 去掉了环境检测和自动设置,命令历史和日志,以及changlog的内容,这些内容可能会在后续版本完成
* 压缩算法会导致 解压缩之后的 文件和之前不一致 会出现最后的 换行符 问题,这个需要良好的解决，但只会出现在一个文件的最后一行
    - 2013年 03月 19日 星期二 19:23:37 CST 该问题的算法，暂时没有一个好的解决方案，由于不影响插件使用，暂时先不修正
* 解压缩算法 导致 空文件不会建立,改变程序可以解决这个问题
    - 2013年 03月 19日 星期二 19:24:58 CST 经过检查，这个问题已经在代码里面解决了
* 兼容现有主流插件管理系统的包或者机制
    - 将github或者bitbucket的代码下载回来 然后自动打包 自动命名
* 对于字段中的空字段还没有处理机制，等查询yaml标准后确定处理方案 
* tools 中的功能需要提取到库中
* 从github打包插件的功能还没完善和测试
* 移除对python非标准库的依赖，比如yaml
* 考虑lazyload插件的功能,以及具体由vimapt自身提供还是由插件提供
* 参考dein.vim和vim-plug和vim-addon-manager的功能
