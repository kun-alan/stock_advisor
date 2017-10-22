<!doctype html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
        <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-red.min.css" />
        <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
        <style>
            .demo-card-square.mdl-card {
                width: 320px;
                height: 320px;
            }
            .demo-card-square > .mdl-card__title {
                color: #fff;
                background: #46B6AC;
            }

            .cards-cell {
                min-height: 187px;
                padding: 8px;
                margin: 5px;
                background-color: #DFFFFF;
            }
            .cards-cell span {
                padding-left: 4px;
                padding-right: 4px;
            }
            .color-plus {
                color: green;
            }
            .color-minus {
                color: red;
            }
            .color-even {
                color: black;
            }
        </style>
    </head>
    <body>
        <div>
            <div class="mdl-tabs mdl-js-tabs">
                <div class="mdl-tabs__tab-bar">
                    % for tab in tabs:
{{!tab}}
                    % end
                </div>

                <div class="mdl-tabs__panel is-active" id="watcher">
                    <div class="mdl-grid">
                        % for card in cards:
                            <div>
{{!card}}
                            </div>
                        % end
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
