#!/usr/bin/env bash
echo $(date -u)";"$(curl -s https://www.coingecko.com/en/coins/bitcoin | grep '<span class="no-wrap" data-price-btc="1.0" data-coin-id="1" data-coin-symbol="btc" data-target="price.price">' | grep -oP '\$\d{1,3}(,\d{3})*\.\d{2}' | sed -n '1p') >> /home/ec2-user/S8-Git_Python_Linux/Projet/PrixBTC.csv
