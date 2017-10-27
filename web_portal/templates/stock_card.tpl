<div class="mdl-cell mdl-cell--4-col">
    <div class="demo-card-square mdl-card mdl-shadow--2dp">
        <div class="mdl-card__title mdl-card--expand">
            <h2 class="mdl-card__title-text">
                <a class="symbol-link" href="https://finance.yahoo.com/quote/{{card.symbol}}?p={{card.symbol}}" target=”_blank”>
                    {{card.symbol}}
                </a>
            </h2>
        </div>
        <div class="cards-cell">
            <span>{{card.price}}</span>
            <span class="{{card.color_class}}">{{card.change}}</span>
            <span class="{{card.color_class}}">({{card.percent_change}}%)</span>
        </div>
        <div class="mdl-card__actions mdl-card--border">
            <a class="mdl-button mdl-button--colored">
            More
            </a>
        </div>
    </div>
</div>
