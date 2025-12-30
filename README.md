## DESCRIPTION :

This project models how wheat, energy, and ethanol price volatility affects the profitability of a wheat-to-bioethanol plant supplying the UK E10 market. Using Monte Carlo simulation, it quantifies financial risk, identifies key cost drivers, and evaluates the likelihood of loss or reduced margins.

## Project Structure
- data/ – raw and processed market data
- src/ – core simulation and economic models
- notebooks/ – exploratory analysis
- outputs/ – figures and results
- tests/ – unit tests

## OBJECTIVES

Assess financial exposure to wheat, ethanol, and energy price fluctuations

Estimate distributions of EBITDA and NPV

Identify the most critical economic risk drivers

Simulate extreme scenarios, such as policy or import shocks

Support data-driven decisions on procurement, hedging, and investment

## BACKGROUND

Bioethanol plants in the UK rely on wheat feedstock and sell ethanol into the E10 petrol blend market. Both feedstock costs and product prices are volatile, creating financial risk. Monte Carlo simulation allows probabilistic assessment of profitability and risk mitigation strategies.

**DATA SOURCES**

Historical UK wheat prices (e.g., AHDB or CME)

Ethanol wholesale prices in the UK

Natural gas/electricity prices for plant energy costs

DDGS/animal feed co-product prices

**METHODOLOGY**

Collect and preprocess historical price data

Fit statistical models for wheat, ethanol, energy, and co-product prices

Simulate thousands of potential future price paths using Monte Carlo methods

Calculate yearly cash flows, EBITDA, and NPV for each scenario

Analyze distributions and compute risk metrics (e.g., probability of negative NPV, Value at Risk)

**USAGE**

Install dependencies: numpy, pandas, matplotlib

Run the Monte Carlo simulation script: python montecarlo_wheat_uk_ethanol.py

Modify plant-specific parameters (capacity, CAPEX, OPEX) in the configuration section of the script

**OUTPUTS**

Histograms of NPV and EBITDA distributions

Probability of loss or negative cash flows

Tornado charts identifying key cost drivers

Scenario analysis results (import shocks, policy changes, crop yield variations)
