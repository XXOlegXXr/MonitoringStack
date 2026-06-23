#Monitoring Stack (Prometheus, Grafana, Alertmanager & Telegram)

This project is ready solution for monotoring as by infrastructure, servers metrics, services, visualisate data from service using promQL, automating push
 alert in Telegram group.The stack is containerized via Docker Compsoe



## That is include to stack?

* **Prometheus** — Prometheus** — collects and stores metrics, calculates notification rules..
* **Grafana** — Visualisate data & create dashboards.
* **Node Exporter** — collect system metrics (CPU, RAM, Disk) with host(in my case WSL2).
* **Alertmanager** — create and push alert from prometheus to Telegram Bot(Apprise).
* **Apprise (Telegram-relay)** — stateless-service for comfortable delivery notification to Telegram.

---

## How run in self?


### 1. Priviose requirements

* Linux(Debian family) / WSL2 (Ubuntu)
* Docker та Docker Compose

### 2. Clone monitoring_stack


```bash

git clone <https://github.com/XXOlegXXr/MonitoringStack.git>
cd monitor_stack
docker compose up



### 3. Create .env

For Example

TELEGRAM_BOT_TOKEN=8849732162:AAGpCVqu76m4Q...
TELEGRAM_CHAT_ID=32464353246


Token you shoud claim in Telegram(BotFather)
   
CHAT_ID - show in webpage into massive JSON key


### Acces web UI

Grafana: <http://localhost:3000> (Login/Password by defoult: admin/admin)

Prometheus: <http://localhost:9090>

Alertmanager: <http://localhost:9093>


### Config Telegram alert

```bash

curl -X POST http://localhost:8000/add/alerts \
  -d "urls=tgram://${TELEGRAM_BOT_TOKEN}/${TELEGRAM_CHAT_ID}/"

# BOT: @oleg_monitoring_alerts_bot
```

<img width="1229" height="934" alt="Знімок екрана 2026-06-23 212103" src="https://github.com/user-attachments/assets/036f454b-028f-4f1e-8417-2cdcdb27c6e7" />

<img width="1919" height="908" alt="Знімок екрана 2026-06-23 212308" src="https://github.com/user-attachments/assets/8b182a6f-28db-4b3f-bd8d-f4bc27631d80" />

<img width="1919" height="926" alt="Знімок екрана 2026-06-23 212430" src="https://github.com/user-attachments/assets/8b515520-1408-4690-bbb3-59fc10a11383" />

<img width="1918" height="966" alt="Знімок екрана 2026-06-23 212458" src="https://github.com/user-attachments/assets/abb0d2ca-217a-4023-bc3d-4af27c0de55b" />




