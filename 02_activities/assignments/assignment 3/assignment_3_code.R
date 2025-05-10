library(readr)
library(ggplot2)

df <- read_csv("W:/DSI/visualization/02_activities/assignments/assignment_3/wellbeing_toronto.csv")

colnames(df)

model <- lm(`Healthy Food Index` ~ `Early Development Instrument (EDI)`, data = df)
summary(model)

# Extract coefficients
intercept <- coef(model)[1]
slope <- coef(model)[2]

# Create labeled regression equation
reg_eq <- paste0("EDI = ", round(intercept, 2), " + ", round(slope, 2), " × Healthy Food Index")


ggplot(df, aes(x = `Early Development Instrument (EDI)`, y = `Healthy Food Index`)) +
  geom_point(color = "steelblue", alpha = 0.7, size = 3) +
  geom_smooth(method = "lm", se = TRUE, color = "darkred", linetype = "dashed") +
  annotate("text", x = min(df$`Early Development Instrument (EDI)`), y = max(df$`Healthy Food Index`),
           label = reg_eq, hjust = 0, vjust = 1.5, size = 5, fontface = "italic", color = "darkred") +
  labs(
    title = "Linear Regression: Healthy Food Index vs. EDI Score Across Toronto Neighbours",
    x = "Early Development Instrument Score (EDI)",
    y = "Healthy Food Index"
  ) +
  theme_minimal()
