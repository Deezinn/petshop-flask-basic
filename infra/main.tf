provider "azurerm" {
  features {}
  subscription_id = "62a47bad-99aa-450d-a7e2-ef75d08015f4"
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-petshop"
  location = "Brazil South"
}

resource "azurerm_app_service_plan" "plan" {
  name                = "asp-petshop"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

    kind     = "Linux"
  reserved = true
  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_linux_web_app" "app" {
  name = "petshop-flask-app-deezinn123456"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_app_service_plan.plan.id

    site_config {
    application_stack {
        python_version = "3.10"
    }
    }



  app_settings = {
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    "SCM_DO_BUILD_DURING_DEPLOYMENT"      = "true"
    "GITHUB_REPO"                         = "Deezinn/petshop-flask-basic"
    "FLASK_ENV"                           = "production"
  }

  identity {
    type = "SystemAssigned"
  }
}
