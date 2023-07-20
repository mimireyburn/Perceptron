An ML project for the MLX2 Founders and Coders level 7 AI apprenticeship: recommendation system

## How to run

1. Install tilt: `curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash`
2. Copy the env `cp .env.example .env` and set environment variables
3. Start `tilt up`

## Architecture
<img width="772" alt="Screenshot 2023-07-20 at 13 32 02" src="https://github.com/mimireyburn/Perceptron/assets/36554605/2a122672-eff3-4878-8981-d01e271bb8bf">

Serices: 
- app
- db (postgres)
- cache (redis)
- kafka
- zookeeper
- workers
