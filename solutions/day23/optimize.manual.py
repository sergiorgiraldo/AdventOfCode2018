
        # returns the 8 corners of the cube of coordinates in range for the bot 
    def get_corners(self,nanobot):
        r = nanobot[3]
        corners = []
            
        for dx in [-r, r]:
            for dy in [-r, r]:
                for dz in [-r, r]:
                    corners.append((nanobot[0]+dx, nanobot[1]+dy, nanobot[2]+dz))
        return corners

    def get_close_to_nanobots(self, lines):
        nanobots = self.parse(lines)
        #start looking for the best point around the nanobots
        all_corners = set().union([(0, 0, 0)], *[self.get_corners(bot) for bot in nanobots])
        best_coverage = -1
        best_distance = None
        best_point = None

        # Find initial decent solution
        for point in all_corners:
            coverage = len([bot for bot in nanobots if self.get_manhattan_distance(point, bot) <= bot[3]])
            distance = self.get_manhattan_distance(point, (0, 0, 0))
            if coverage > best_coverage or (coverage == best_coverage and distance < best_distance):
                best_coverage = coverage
                best_point = point
                best_distance = self.get_manhattan_distance(point, (0, 0, 0))

        print(best_distance, best_point, best_coverage)

        max_displacement = 1 << 20
        no_improvement_count = 0
        print("\n>>", max_displacement)
        while True:
            if no_improvement_count > 10000:
                no_improvement_count = 0
                max_displacement /= 2
                print("\n>>", max_displacement)
                if max_displacement < 1:
                    break

            max_displacement = int(max_displacement) #cast to use randint       
            dx = randint(-max_displacement, max_displacement)
            dy = randint(-max_displacement, max_displacement)
            dz = randint(-max_displacement, max_displacement)
            point = (best_point[0]+dx, best_point[1]+dy, best_point[2]+dz)
            coverage = len([bot for bot in nanobots if self.get_manhattan_distance(point, bot) <= bot[3]])
            distance = self.get_manhattan_distance(point, (0, 0, 0))
            if coverage > best_coverage or (coverage == best_coverage and distance < best_distance) or (coverage == best_coverage and distance == best_distance and point < best_point):
                best_coverage = coverage
                best_point = point
                best_distance = self.get_manhattan_distance(point, (0, 0, 0))
                no_improvement_count = 0
            
            no_improvement_count += 1

        print(best_distance, best_point, best_coverage)

        return best_distance