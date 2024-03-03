'''
DISREGARD THIS FILE
DISREGARD THIS FILE
DISREGARD THIS FILE
DISREGARD THIS FILE
DISREGARD THIS FILE
DISREGARD THIS FILE
DISREGARD THIS FILE
'''


library(readr)

find_unique_models <- function(csvFile) {
  data <- read_csv(csvFile)
  modelName <- unique(data$t_model)

  radius <- unique(data$t_rd / 2)
  return(list(modelName, radius))
}

main <- function() {
  csvFile <- "USTurbineData.csv" 
  uniqueValues <- find_unique_models(csvFile)
  
  cat("Unique Models and Radius:\n")
  for (i in seq_along(uniqueValues[[1]])) {
    cat("Model: ", uniqueValues[[1]][i], ", Radius: ", uniqueValues[[2]][i], "\n")
  }
}

main()
