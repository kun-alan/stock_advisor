<div class="mdl-tabs__tab-bar">
    % for tab in tabs:
        <a href="{{tab.href}}" class="mdl-tabs__tab{{tab.active}}">{{tab.text}}</a>
    % end
</div>
<div class="mdl-tabs__tab-bar">
    % for tab in subtabs:
        <a href="{{tab.href}}" class="mdl-tabs__tab{{tab.active}}">{{tab.text}}</a>
    % end
</div>
