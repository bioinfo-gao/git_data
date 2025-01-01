# R Statistics Essential Training
# Ex04_06_Solution
# Transforming skewed data

# Import data
#xskew <- read.csv("~/Desktop/R/xskew.csv")
# https://stats.stackexchange.com/questions/89179/real-life-examples-of-distributions-with-negative-skewness
x      <- c(565, 116, 69, 78, 319, 501, 633, 655, 848, 1226, 1633, 2459, 3375, 4669, 6152, 7436, 9526, 12619, 12455, 7113, 2104, 241)
Breaks <- c(0, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110)



install.packages(c("Hmisc", "ash"))
install.packages("HistogramTools", repos = "http://R-Forge.R-project.org")
#install.packages("HistogramTools")
library(HistogramTools)

#Counts <- c(565, 116, 69, 78, 319, 501, 633, 655, 848, 1226, 1633, 2459, 3375, 4669, 6152, 7436, 9526, 12619, 12455, 7113, 2104, 241)
Counts <- c(56, 116, 69, 78, 319, 501, 633, 655, 848, 1226, 1633, 2459, 3375, 4669, 6152, 7436, 9526, 12619, 12455, 7113, 2104, 241)
Breaks <- c(0, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110)

myhist <- PreBinnedHistogram(
    breaks = Breaks,
    counts = Counts,
    xname = "pep of Australian Males, 2012")
plot(myhist)

myhist <- PreBinnedHistogram(
    breaks = Breaks,
    counts = Counts^2,
    xname = "pep of Australian Males, 2012")
plot(myhist)

myhist <- PreBinnedHistogram(
    breaks = Breaks,
    counts = Counts^4,
    xname = "pep of Australian Males, 2012")
plot(myhist)


myhist <- PreBinnedHistogram(
    breaks = Breaks,
    counts = sqrt(Counts),
    xname = "pep of Australian Males, 2012")
plot(myhist)


