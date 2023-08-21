cd Dependencias
helm dependency update
cd ..
cd Elastic-Search
rm -rf Char.lock
helm dependency build --skip-refresh
cd..

helm upgrade --install dependencias dependencias
helm upgrade --install elastic-search elastic-search