import pandas, math

def find_unique_models(file):
    data = pandas.read_csv(file)
    diameters = data[['t_model', 't_rd']]

    models = dict()
    for idx in diameters.index:
        model = diameters['t_model'][idx]
        dia = diameters['t_rd'][idx]
        
        if not math.isnan(dia):
            models[model] = dia / 2


find_unique_models("USTurbineData.csv")    



'''
find_unique_models <- function(csv_file) {
  data <- read_csv("USTurbineData.csv")
  unique_models <- unique(data$t_model)
  return(unique_models)
}
main <- function() {
  csv_file <- "USTurbineData.csv"  
  unique_models <- find_unique_models(csv_file)
cat("Unique Models:\n")
    for (model in unique_models) {
        cat(model, "\n")
 }

}
'''